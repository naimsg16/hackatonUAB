import re

def find_variables(code_string):
    # Define the regular expression pattern for variable names
    pattern = r'(?<!\.)\b[^.][a-zA-Z_][a-zA-Z0-9_]*\b'
    
    # List of Python reserved keywords
    reserved_keywords = {
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    }
    
    # Find all matches in the code string
    matches = re.findall(pattern, code_string)
    
    # Filter out reserved keywords
    variables = [word for word in matches if word not in reserved_keywords]
    
    return variables

# Example usage
code_string = """
def check_comment(token):
    if '#' in token:
        content = token.split('#')
        code = content[0]
        comment = content[1]
        file2.write(f"{code}#{comment.upper()} \n")
    elif token != '':
        file2.write(token + '\n')
    else:
        file2.write('\n')
"""

variables = find_variables(code_string)
print("Variables found:", variables)
