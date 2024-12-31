import argparse

from .config_parser import parse_config
from .terragrunt_executor import execute_terragrunt
from .terragrunt_generator import generate_terragrunt_files


def main():
    parser = argparse.ArgumentParser(description="Generate and execute Terragrunt configurations from YAML.")
    parser.add_argument("-f", "--file", required=True, help="Path to the YAML configuration file.")
    args = parser.parse_args()

    config = parse_config(args.file)
    generate_terragrunt_files(config)
    execute_terragrunt(config)


if __name__ == "__main__":
    main()


# Usage (as python module):
# $ python -m src.cli -f tests/stest.yaml
