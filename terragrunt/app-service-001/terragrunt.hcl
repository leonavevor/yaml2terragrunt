# Terragrunt configuration for app-service-001
include {
  path = find_in_parent_folders()
}
terraform {
  source = "${get_repo_root()}./terraform/.modules//app-service"
  # Add additional configuration here
}
inputs = {
 # Add inputs here
}
