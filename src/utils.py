import re

def evaluate_monstash_expressions(code):
    pattern = r"\{\{(.+?)\}\}"
    matches = re.findall(pattern, code)
    evaluated_code = code
    for match in matches:
        if match.startswith("module."):
            # treat as a module (this i.e: same module)
            pass
        elif match.startswith("dependency."):
            # treat as a dependency
            pass
        elif match.startswith("var."):
            # treat as a variable
            pass
        elif match.startswith("param."):
            # treat as a parameter
            pass
        elif match.startswith("**"):
            # treat as a dictionary
            pass
        else:
            pass
            
    return evaluated_code

# functions to handle the different types of expressions
def evaluate_module_expression(match):
    pass

# funtions to handle implicit dependencies
def evaluate_implicit_dependency_expression(match):
    pass

# functions to handle explicit dependencies
def evaluate_explicit_dependency_expression(match):
    pass

# functions to handle variables
def evaluate_variable_expression(match):
    pass

# functions to handle parameters
def evaluate_parameter_expression(match):
    pass

# functions to handle dictionary expansions
def evaluate_dictionary_expansion(match):
    pass

# handle depends_on
def handle_depends_on(match):
    pass

# handle source
