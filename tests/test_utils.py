import json
import unittest
from unittest.mock import mock_open, patch

import yaml

from src.utils import convert_yaml_to_terragrunt, generate_terragrunt_config


class TestUtils(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="key: value")
    @patch("subprocess.run")
    def test_convert_yaml_to_terragrunt(self, mock_subprocess, mock_file):
        # Mock subprocess run
        mock_subprocess.return_value.stdout = "HCL content"
        mock_subprocess.return_value.returncode = 0

        # Test conversion
        result = convert_yaml_to_terragrunt("test.yaml")
        self.assertEqual(result, "HCL content")

        # Ensure file was opened
        mock_file.assert_called_once_with("test.yaml", "r")

    def test_generate_terragrunt_config(self):
        yaml_config = {"source": "some-source", "inputs": {"key": "value"}, "backend": "s3", "bucket": "my-bucket", "key": "my-key", "region": "us-west-2"}
        expected_hcl = """
# Auto-generated Terragrunt configuration
terraform {{
  source = "some-source"
}}

inputs = {{
{
  "key": "value"
}
}}

remote_state {{
  backend = "s3"
  config = {{
    bucket = "my-bucket"
    key    = "my-key"
    region = "us-west-2"
  }}
}}
"""
        result = generate_terragrunt_config(yaml_config)
        self.assertEqual(result.strip(), expected_hcl.strip())


if __name__ == "__main__":
    unittest.main()
