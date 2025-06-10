# Day 11 - Functions
import keyword

def is_valid_python_variable_name(variable_name: str) -> bool:
    """
    Checks if the provided string is a valid Python variable name.

    A valid Python variable name must:
    1. Start with a letter (a-z, A-Z) or an underscore (_).
    2. Contain only alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
    3. Not be a Python keyword (e.g., 'if', 'for', 'class').

    Args:
        variable_name (str): The string to check.

    Returns:
        bool: True if the string is a valid Python variable name, False otherwise.
    """
    if not isinstance(variable_name, str):
        # Handle cases where the input is not a string
        print(f"Warning: Input '{variable_name}' is not a string. Returning False.")
        return False

    # Check if it's a valid Python identifier (syntax check)
    # This checks for valid starting character and allowed characters.
    if not variable_name.isidentifier():
        return False

    # Check if it's a Python keyword
    # Keywords cannot be used as variable names.
    if keyword.iskeyword(variable_name):
        return False

    # If it passes both checks, it's a valid variable name
    return True
