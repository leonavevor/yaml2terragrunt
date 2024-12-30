import argparse
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from src.main import main


class TestMain(unittest.TestCase):
    @patch("src.main.convert_yaml_to_terragrunt")
    @patch("argparse.ArgumentParser.parse_args")
    def test_main_with_output(self, mock_parse_args, mock_convert):
        # Mock command line arguments
        mock_parse_args.return_value = argparse.Namespace(yaml_path="test.yaml", output="output.hcl")
        mock_convert.return_value = "HCL content"

        # Capture the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            self.assertIn("Converted HCL written to output.hcl", fake_out.getvalue())

    @patch("src.main.convert_yaml_to_terragrunt")
    @patch("argparse.ArgumentParser.parse_args")
    def test_main_without_output(self, mock_parse_args, mock_convert):
        # Mock command line arguments
        mock_parse_args.return_value = argparse.Namespace(yaml_path="test.yaml", output=None)
        mock_convert.return_value = "HCL content"

        # Capture the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            self.assertIn("HCL content", fake_out.getvalue())


if __name__ == "__main__":
    unittest.main()

# Usage (use main as a module):
# $ python -m src.main tests/test.yaml
