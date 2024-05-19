from variable_seeker import find_variables
import re
from deep_translator import GoogleTranslator
from langdetect import detect

languages = {
    'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali', 'ca': 'Catalan', 'cs': 'Czech',
'cy': 'Welsh', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish',
'et': 'Estonian', 'fa': 'Persian (Farsi)', 'fi': 'Finnish', 'fr': 'French', 'gu': 'Gujarati', 'he': 'Hebrew',
'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
'kn': 'Kannada', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mk': 'Macedonian', 'ml': 'Malayalam',
'mr': 'Marathi', 'ne': 'Nepali', 'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi', 'pl': 'Polish',
'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali',
'sq': 'Albanian', 'sv': 'Swedish', 'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai',
'tl': 'Tagalog', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'vi': 'Vietnamese', 'zh-cn': 'Chinese (Simplified)',
'zh-tw': 'Chinese (Traditional)'
}

language_names = {v.lower(): k for k, v in languages.items()}           # Crear un diccionario inverso para buscar por nombre de idioma

print("Enter the name of the language you want for the translation:")   # Pedir al usuario que ingrese el nombre del idioma deseado
input_language = input().strip().lower()

if input_language not in language_names:                                # Validar si el nombre del idioma ingresado es válido
    print("Invalid language name. Please restart the program and enter a valid name.")
    exit()

lang = language_names[input_language]                                   # Obtener el código del idioma correspondiente

traductor = GoogleTranslator(source='auto', target=lang)                # Configurar el traductor con el idioma seleccionado

def process_line (token):
    """ if "import" in token:  
        # Si detecta que es un import, ignora el procés
        line = token 
    else: """
        # En altre cas, ho tradueix
    line = translate(token)
    output.write(line + '\n')


def translate (line):
    variables = find_variables(line)    # Aquí guardem les variables trobades
    pattern = r'\(|\)|\:|\w+|\s+|[^\w\s]'  
    words = re.findall(pattern,line)    # Fem un split i separem tots els caràcters
    translated = ""
    for word in words:                  # Per cada paraula del split:
        if word in variables:           
            new_word = traductor.translate(word)    # Si està a les variables, la canviem TODO
            
        else:
            new_word = word             # Si no, la deixem igual
        translated += new_word          # Afegim la nova paraula
    return translated                   # Retornem la traducció



if __name__=="__main__":     
    with open("prova.py","r", encoding="utf-8") as input:
        # Llegim el codi
        lines = input.readlines()
    with open("output.py","a", encoding="utf-8") as output:
        # Resetejem el output
        output.truncate(0)
        for line in lines:
            tokenized =  line.split('\n')   # Separem les línies
            process_line(tokenized[0])