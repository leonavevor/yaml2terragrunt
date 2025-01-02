import os
import yaml
import jinja2

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def render_template(template_str, context):
    template = jinja2.Template(template_str)
    return template.render(context)

def create_directory_structure(base_path, modules):
    for module in modules:
        module_path = os.path.join(base_path, module['name'])
        os.makedirs(module_path, exist_ok=True)

def create_terragrunt_hcl(module, context):
    hcl_template = """
    terraform {
      source = "{{ module.source }}"
    }

    inputs = {
      {% for key, value in module.inputs.items() %}
      {{ key }} = "{{ value }}"
      {% endfor %}
    }

    outputs = {
      {% for key, value in module.outputs.items() %}
      {{ key }} = "{{ value }}"
      {% endfor %}
    }

    {% if module.depends_on %}
    dependencies {
      paths = [
        {% for dependency in module.depends_on %}
        "{{ dependency }}",
        {% endfor %}
      ]
    }
    {% endif %}

    {% if module.dependencies %}
    dependency {
      config_path = "{{ module.dependencies.config_path }}"
      mock_outputs = {
        {% for key, value in module.dependencies.mock_outputs.items() %}
        {{ key }} = "{{ value }}"
        {% endfor %}
      }
    }
    {% endif %}

    {% if module.hooks %}
    hooks {
      {% for hook in module.hooks %}
      {{ hook.type }} {
        commands = [
          "{{ hook.command }}"
        ]
      }
      {% endfor %}
    }
    {% endif %}

    {% if module.retries %}
    retry {
      max_retries = {{ module.retries.max_retries }}
      delay = {{ module.retries.delay }}
      backoff = {{ module.retries.backoff }}
      error_pattern = "{{ module.retries.error_pattern }}"
    }
    {% endif %}
    """
    return render_template(hcl_template, context)

def main(yaml_file):
    config = load_yaml(yaml_file)
    base_path = os.path.dirname(yaml_file)

    create_directory_structure(base_path, config['modules'])

    for module in config['modules']:
        context = {
            'module': module,
            'param': config['parameters'],
            'var': config['globals']['vars'],
            'environment': config['globals']['environment']
        }
        hcl_content = create_terragrunt_hcl(module, context)
        hcl_file_path = os.path.join(base_path, module['name'], 'terragrunt.hcl')
        with open(hcl_file_path, 'w') as hcl_file:
            hcl_file.write(hcl_content)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Terragrunt configuration from YAML")
    parser.add_argument("-f", "--file", required=True, help="Path to the YAML configuration file")
    args = parser.parse_args()
    main(args.file)
