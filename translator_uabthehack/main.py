import re
import variable_seeker
from deep_translator import GoogleTranslator
import sys



def process_line (token, toggle, traductor, output):
    if '#' in token:
        content = token.split('#')
        code = translate(content[0], traductor)
        comment = content[1]
        trns_comment = traductor.translate(comment)
        output.write(f"{code} # {trns_comment}\n")
    elif toggle == True:
        doc = traductor.translate(token) 
        output.write( doc + "\n")
    elif token != '':
        trns_code = translate(token, traductor) 
        output.write(trns_code + "\n")
    else:
        output.write('\n')


def translate (line, traductor):
    variables = variable_seeker.find_variables(line)    # Aquí guardem les variables trobades
    pattern = r'\(|\)|\:|\w+|\s+|[^\w\s]'  
    words = re.findall(pattern,line)  # Fem un split i separem tots els caràcters
    translated = ""
    for word in words:                  # Per cada paraula del split:
        if word in variables:           
            literal_trns = traductor.translate(word).split()     
            # Si està a les variables, la canviem
            new_word = '_'.join(literal_trns)
        else:
            new_word = word             # Si no, la deixem igual
        translated += new_word          # Afegim la nova paraula
    return translated                   # Retornem la traducció

def translate_code(input_file, trans_language, output_file):


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
    input_language = trans_language.strip().lower()
    if input_language not in language_names:                                # Validar si el nombre del idioma ingresado es válido
        print("Invalid language name. Please restart the program and enter a valid name.")
        exit()

    lang = language_names[input_language]                                   # Obtener el código del idioma correspondiente
    
    traductor = GoogleTranslator(source='auto', target=lang)                # Configurar el traductor con el idioma seleccionado


    with open(input_file,"r", encoding="utf-8") as input:
        # Llegim el codi
        lines = input.readlines()
    with open(output_file,"a", encoding="utf-8") as output:
        # Resetejem el output
        output.truncate(0)
        toggle = False
        for line in lines:
            if "import" in line:
                output.write(line + "\n")
                words = line.split()
                for word in words:
                    variable_seeker.add_keyword(word)
            else:
                tokenized =  line.split('\n')   # Separem les línies
                text = tokenized[0]
                if(text == "\"\"\"" or text == "\'\'\'"):
                    toggle = not toggle
                    output.write(text + "\n")
                else:
                    process_line(text, toggle, traductor, output)

if __name__=="__main__":    
    translate_code(sys.argv[1],sys.argv[2], sys.argv[3])