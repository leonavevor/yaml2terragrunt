import argparse

from .utils import convert_yaml_to_terragrunt  # noqa: F401


def main():
    parser = argparse.ArgumentParser(description="Convert YAML to Terragrunt HCL")
    parser.add_argument("yaml_path", help="Path to the input YAML file")
    parser.add_argument("-o", "--output", help="Path to the output HCL file", default=None)

    args = parser.parse_args()

    hcl_output = convert_yaml_to_terragrunt(args.yaml_path, args.output)
    if args.output:
        print(f"Converted HCL written to {args.output}")
    else:
        print(hcl_output)


if __name__ == "__main__":
    main()
