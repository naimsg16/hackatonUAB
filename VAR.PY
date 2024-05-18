import re

def find_variables(code_string):
    # Define the regular expression pattern for variable names
    pattern = r'(?<![."\'\w])\b[a-zA-Z_][a-zA-Z0-9_]{1,}\b'
    
    # List of Python reserved keywords
    reserved_keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 'print'
    }
    
    # Find all matches in the code string
    matches = re.findall(pattern, code_string)
    
    # Filter out reserved keywords
    variables = [word for word in matches if word not in reserved_keywords]
    
    return variables

# Example usage
code_string = """
import random

print("hola")
print()

natGUarra = 3
while(n > 8):
    n += 1
    print('hello')
"""


variables = find_variables(code_string)
print("Variables found:", variables)
