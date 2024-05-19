import re
reserved_keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 
        'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
        'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
        'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
        'raise', 'return', 'try', 'while', 'with', 'yield', 'int', 'list','bool', 'str',
        'set', 'dict', 'tuple', 'float', 'self', 'sum', 'print', 'any', 'all', 'max', 'len', 
        'min', 'sorted', 'reversed', 'enumerate', 'filter', 'map', 'zip', '__name__', 'open','r'
    ]

def find_variables(code_string):
    # Define the regular expression pattern for variable names
    pattern = r'(?<![."\'\w])\b[\w][\w]*\b'
    
    # Find all matches in the code string
    matches = re.findall(pattern, code_string, re.UNICODE)
    
    # Filter out reserved keywords
    variables = [word for word in matches if word not in reserved_keywords]
    
    variables2 = set(variables)
    return variables2

def add_keyword (line):
    reserved_keywords.append(line)