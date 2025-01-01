import json
import os
import subprocess
from jinja2 import Template


def load_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def render_template(template_str, context):
    template = Template(template_str)
    return template.render(context)


def generate_terragrunt_files(config, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for module in config["modules"]:
        module_name = module["name"]
        module_dir = os.path.join(output_dir, module_name)
        os.makedirs(module_dir, exist_ok=True)

        hcl_content = render_template(module_template, module)
        with open(os.path.join(module_dir, "terragrunt.hcl"), "w") as file:
            file.write(hcl_content)


def execute_terragrunt(root_path, action):
    subprocess.run(["terragrunt", action], cwd=root_path)


module_template = """
terraform {
  source = "{{ source }}"
}

inputs = {
{% for key, value in inputs.items() %}
  {{ key }} = "{{ value }}"
{% endfor %}
}

{% if depends_on %}
dependencies {
  paths = [
  {% for dep in depends_on %}
    "{{ dep }}",
  {% endfor %}
  ]
}
{% endif %}
"""

if __name__ == "__main__":
    config_path = "./tests/sample_tg_declaration.json"
    output_dir = "../terragrunt"

    config = load_config(config_path)
    generate_terragrunt_files(config, output_dir)
    execute_terragrunt(output_dir, "apply")
