### Purpose: 
yaml2terragrunt is an open-source project designed to enable the dynamic creation of Terragrunt files, folders, and configurations using a declarative YAML approach. The primary objective is to simplify and streamline the management of complex infrastructure-as-code setups, particularly for organizations dealing with multiple environments, regions, and services.


### Aim:
The project aims to address several shortcomings of traditional Terragrunt folder structures:

1. Scalability issues: As projects grow, maintaining a consistent folder structure across multiple environments and regions becomes challenging.

2. Duplication of code: Traditional approaches often lead to repetitive configurations, violating the DRY (Don't Repeat Yourself) principle.

3. Limited flexibility: Static configurations make it difficult to share complex variables or computed values across different levels of the hierarchy.

4. Complexity in reorganization: Restructuring existing Terragrunt projects can be cumbersome and error-prone.


### Future objectives:
Future objectives for yaml2terragrunt may include:

1. Enhancing support for multi-region and multi-environment setups.
2. Implementing advanced features for dynamic configuration generation.
3. Developing tools to facilitate easier migration from existing Terragrunt structures.
4. Improving integration with other infrastructure-as-code tools and workflows.

### Summary:
By addressing these challenges, yaml2terragrunt aims to provide a more flexible, maintainable, and scalable approach to managing Terragrunt configurations for complex infrastructure projects.

## Recommended Workflow
Create YAML configuration files with a standard structure
Use the Python script to convert YAML to Terragrunt HCL
Run Terragrunt/Terraform as normal with generated HCL files

### Example YAML Configuration:
```yaml
source: "github.com/module/path"
backend: "s3"
bucket: "my-terraform-state"
key: "environment/component"
region: "us-west-2"
inputs:
  instance_type: "t3.micro"
  environment: "staging"
```

### Considerations and Limitations
Requires PyYAML and potentially tfmt for JSON to HCL conversion
Complex configurations might need manual tweaking
Performance overhead of conversion

### Dependencies:
- PyYAML
- tfmt (optional, for JSON to HCL conversion)
- Python 3.7+


### Potential Enhancements:
- Add robust error handling
- Support for complex Terragrunt inheritance
- Validation against Terraform schemas
- Templating support

### Contributing:
[Contribution guidelines for this project](.github/CONTRIBUTING.md)
