import json
import os
import subprocess

from jinja2 import Template


def load_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# TODO: make use of jinja2 instead to make rendering easier, so just return the object and render it in the main function
def build_child_locals(context: dict) -> str:
    for key, value in context["locals"].items():
        locals += f'{key} = "{value}",\n'
    locals_builder = f"""
    locals = {{
        {locals}
    }}
    """
    return locals_builder


# TODO: make use of jinja2 instead to make rendering easier, so just return the object and render it in the main function
def build_child_include_root(context: dict) -> str:
    return """
    include "root" {
        path = find_in_parent_folders("root.hcl")
    }
    """


# TODO: make use of jinja2 instead to make rendering easier, so just return the object and render it in the main function
def build_child_implicit_dependencies(context: dict, output_dir: str) -> str:
    implicit_dep_builder: str = ""
    # handle implicit dependencies (but try to respect the explicit ones)
    if "dependency." in context["source"]:
        # foreach module in context, consider each module as a path
        for context["dep"] in context["source"]:
            dep = context["source"].replace("dependency.", "")
            dep_path = os.path.join(f"{output_dir + '/' + context['dep']}", "terragrunt.hcl")
            if os.path.exists(dep_path):
                implicit_dep_builder = f"""
                dependency "{ dep }" {{
                    config_path = "{dep_path}/terragrunt.hcl"
                }}
                """
    return implicit_dep_builder


# TODO: make use of jinja2 instead to make rendering easier, so just return the object and render it in the main function
def build_child_explicit_dependencies(context: dict) -> str:
    # handle explicit dependencies, this will help arrange the order of execution of the modules
    explicit_dep_builder: str = ""
    if "depends_on" in context:
        for dep in context["depends_on"]:
            deps += dep.replace("module.", "") + ", "
        dep_list = deps.rstrip(", ")
        explicit_dep_builder = f"""
        dependencies {{
            paths = [
                {dep_list}
            ]
        }}
        """
    return explicit_dep_builder


# TODO: make use of jinja2 instead to make rendering easier, so just return the object and render it in the main function
def build_child_inputs(context: dict) -> str:
    # handle inputs
    inputs_builder: str = ""
    if "inputs" in context:
        for key, value in context["inputs"].items():
            inputs += f'{key} = "{value}",\n'
        inputs_builder = f"""
        inputs = {{
            {inputs}
        }}
        """
    return inputs_builder


def render_template(template_str, context):
    template = Template(template_str)
    return template.render(context)


def generate_terragrunt_files(config, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for module in config["modules"]:
        module_name = module["name"]
        module_dir = os.path.join(output_dir, module_name)
        os.makedirs(module_dir, exist_ok=True)

        hcl_content = render_template(module_child_template, module)
        with open(os.path.join(module_dir, "terragrunt.hcl"), "w") as file:
            file.write(hcl_content)


def execute_terragrunt(root_path, action):
    subprocess.run(["terragrunt", action], cwd=root_path)


module_child_template = """

{% if locals %}
locals {
  {% for key, value in locals.items() %}
    {{ key }} = "{{ value }}"
  {% endfor %}
}
{% endif %}

terraform {
  source = "{{ source }}"
}


{% for name, path in dependencies.items() %}
dependency "{{ name }}" {
  config_path = "{{ path }}"
}
{% endfor %}


{% if depends_on %}
dependencies {
  paths = [
  {% for dep in depends_on %}
    "{{ dep }}",
  {% endfor %}
  ]
}
{% endif %}

# retries

# hooks (do in parent instead)

inputs = {
{% for key, value in inputs.items() %}
  {{ key }} = "{{ value }}"
{% endfor %}
}
"""

if __name__ == "__main__":
    config_path = "./tests/sample_tg_declaration.json"
    output_dir = "../terragrunt"

    config = load_config(config_path)
    generate_terragrunt_files(config, output_dir)
    execute_terragrunt(output_dir, "apply")
