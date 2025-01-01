import argparse
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from src.cli import main


class TestMain(unittest.TestCase):
    @patch("src.cli.parse_config")
    @patch("src.cli.generate_terragrunt_files")
    @patch("src.cli.execute_terragrunt")
    def test_main(
        self, mock_execute_terragrunt, mock_generate_terragrunt_files, mock_parse_config
    ):
        with patch.object(
            sys, "argv", ["cli.py", "-f", "./src/tests/sample_tg_declaration.yaml"]
        ):
            main()
            mock_parse_config.assert_called_once_with(
                "./src/tests/sample_tg_declaration.yaml"
            )
            mock_generate_terragrunt_files.assert_called_once()
            mock_execute_terragrunt.assert_called_once()

    @patch("src.cli.parse_config")
    @patch("src.cli.generate_terragrunt_files")
    @patch("src.cli.execute_terragrunt")
    def test_main_no_args(
        self, mock_execute_terragrunt, mock_generate_terragrunt_files, mock_parse_config
    ):
        with patch.object(sys, "argv", ["cli.py"]):
            with self.assertRaises(SystemExit):
                main()
                mock_parse_config.assert_not_called()
                mock_generate_terragrunt_files.assert_not_called()
                mock_execute_terragrunt.assert_not_called()


if __name__ == "__main__":
    unittest.main()
