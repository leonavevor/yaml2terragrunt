import argparse

from src.config_parser import parse_config
from src.terragrunt_executor import execute_terragrunt
from src.terragrunt_generator import generate_terragrunt_files


def main():
    parser = argparse.ArgumentParser(
        description="Generate and execute Terragrunt configurations from YAML."
    )
    parser.add_argument(
        "-f", "--file", required=True, help="Path to the YAML configuration file."
    )
    args = parser.parse_args()

    config = parse_config(args.file)
    generate_terragrunt_files(config)

    # Add more configuration based on the module inputs and outputs
    execute_terragrunt(
        config=config,
        root_path="./terragrunt/",
        action="plan",
        fail_fast=True,
        # kwargs={"--terragrunt-working-dir": "./"},
    )


if __name__ == "__main__":
    main()


# Usage (as python module):
# $ python -m src.cli -f ./src/tests/sample_tg_declaration.yaml
