# Terragrunt configuration for nsg-subnet-001
include {
  path = find_in_parent_folders()
}
terraform {
  source = "git::github.com/module//nsg?ref=v1.0.0"
 # Add additional configuration here
}
inputs = {
 # Add inputs here
}
