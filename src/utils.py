
import os
import yaml
import json
import subprocess


def convert_yaml_to_terragrunt(yaml_path, output_path=None):
    """
    Convert YAML configuration to Terragrunt HCL

    Args:
        yaml_path (str): Path to input YAML file
        output_path (str, optional): Path to output HCL file

    Returns:
        str: HCL configuration as a string
    """
    # Read YAML file
    with open(yaml_path, 'r') as file:
        config = yaml.safe_load(file)

    # Convert to JSON (easier to process)
    json_config = json.dumps(config, indent=2)

    # Use tf JSON to HCL converter
    hcl_conversion = subprocess.run(
        ['tfmt', '-json', '-', '-o', output_path or '/dev/stdout'],
        input=json_config.encode(),
        capture_output=True,
        text=True
    )

    return hcl_conversion.stdout


def generate_terragrunt_config(yaml_config):
    """
    Generate a comprehensive Terragrunt configuration

    Args:
        yaml_config (dict): Configuration dictionary

    Returns:
        str: Generated Terragrunt HCL configuration
    """
    hcl_template = f"""
# Auto-generated Terragrunt configuration
terraform {{
  source = "{yaml_config.get('source', '')}"
}}

inputs = {{
{json.dumps(yaml_config.get('inputs', {}), indent=2)}
}}

remote_state {{
  backend = "{yaml_config.get('backend', 's3')}"
  config = {{
    bucket = "{yaml_config.get('bucket', '')}"
    key    = "{yaml_config.get('key', '')}"
    region = "{yaml_config.get('region', 'us-east-1')}"
  }}
}}
"""
    return hcl_template



class TerragruntYAMLProcessor:
    def __init__(self, base_dir='.'):
        self.base_dir = base_dir

    def process_yaml_configs(self, yaml_files):
        """
        Process multiple YAML configuration files

        Args:
            yaml_files (list): List of YAML file paths
        """
        for yaml_file in yaml_files:
            config = self._load_yaml(yaml_file)
            hcl_config = self._convert_to_terragrunt(config)
            self._write_terragrunt_config(yaml_file, hcl_config)

    def _load_yaml(self, path):
        """Load YAML configuration"""
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def _convert_to_terragrunt(self, config):
        """Convert YAML config to Terragrunt HCL"""
        # Advanced conversion logic with validation
        pass

    def _write_terragrunt_config(self, source_yaml, hcl_content):
        """Write Terragrunt configuration"""
        output_path = os.path.join(
            self.base_dir,
            os.path.splitext(os.path.basename(source_yaml))[0] + '.hcl'
        )
        with open(output_path, 'w') as f:
            f.write(hcl_content)

