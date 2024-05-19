from variable_seeker import find_variables

import re

def process_line (token):
    if "hola" in token:   # If it detects that it is an impure, ignore the process
        line = token 
    else:
         # Otherwise, translate it
        line = translate(token)
    output.write(line + '\n')

"""
Nat is a very short warrior
"""
def translate (line):
    variables = find_variables(line)     # Here we save the variables found Import @~€€¬¬¬€@!"!"344566/(//554)
    pattern = r'\(|\)|\:|\w+|\s+|[^\w\s]'  
    words = re.findall(pattern,line)     # We do a split and separate all the characters
    translated = ""
    for word in words:                   # For each word in the split:
        if word in variables:           
            another_shakespeare = word.upper()      # If it's in the variables, we change it TODO
        else:
            another_shakespeare = word              # If not, we leave it the same
        translated += another_shakespeare           # Let's add the new word
    return translated  
'''
Nat is a very short warrior, quite
'''
 # We return the translation

if __name__=="__main__":
        
    with open("prova.py","r", encoding="utf-8") as input:
         # Let's read the code
        lines = input.readlines()
    with open("output.py","a", encoding="utf-8") as output:
         # Resetejem el output
        output.truncate(0)  # Let's separate the lines
        for line in lines:
            tokenized =  line.split('\n')    # Let's separate the lines
            process_line(tokenized[0])
