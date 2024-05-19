from variable_seeker import find_variables
import re
def process_line (token):
    if "hola" in token:  # Si detecta que es un impurt, ignora el procés
        line = token 
    else:
        # En altre cas, ho tradueix
        line = translate(token)
    output.write(line + '\n')

"""
La Nat és una guerrera muy bajita
"""
def translate (line):
    variables = find_variables(line)    # Aquí guardem les variables trobades Impotrt @~€€¬¬¬€@!"!"344566/(//554)
    pattern = r'\(|\)|\:|\w+|\s+|[^\w\s]'  
    words = re.findall(pattern,line)    # Fem un split i separem tots els caràcters
    translated = ""
    for word in words:                  # Per cada paraula del split:
        if word in variables:           
            another_shakespeare = word.upper()     # Si està a les variables, la canviem TODO
        else:
            another_shakespeare = word             # Si no, la deixem igual
        translated += another_shakespeare          # Afegim la nova paraula
    return translated  
'''
La Nat es una guerrera muy bajita, bastante
'''
# Retornem la traducció

if __name__=="__main__":
        
    with open("prova.py","r", encoding="utf-8") as input:
        # Llegim el codi
        lines = input.readlines()
    with open("output.py","a", encoding="utf-8") as output:
        # Resetejem el output
        output.truncate(0) # Separem les línies
        for line in lines:
            tokenized =  line.split('\n')   # Separem les línies
            process_line(tokenized[0])