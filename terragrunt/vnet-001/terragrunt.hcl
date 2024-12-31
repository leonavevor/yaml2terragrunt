# Terragrunt configuration for vnet-001
include {
  path = find_in_parent_folders()
}
terraform {
  source = "${get_repo_root()}./terraform/.modules//vnet"
  # Add additional configuration here
}
inputs = {
 # Add inputs here
}
