# Terragrunt configuration for resource-group-001
include {
  path = find_in_parent_folders()
}
terraform {
  source = "git::github.com/module//resource-group?ref=v1.0.0"
 # Add additional configuration here
}
inputs = {
 # Add inputs here
}
