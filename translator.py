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

def check_comment (token):
    if '#' in token:
        content = token.split('#')
        code = content[0]
        comment = content[1]

        detected_language = detect(comment)
        print(detected_language)
        
        translated = traductor.translate(comment)

        file2.write(f"{code}#{translated} \n")

    elif token != '':
        file2.write(token + '\n')
    else:
        file2.write('\n')


if __name__=="__main__":            
    with open("prova.py","r", encoding="utf-8") as file:
        lines = file.readlines()
    
    with open("output.py","a", encoding="utf-8") as file2:
        file2.truncate(0)
        for line in lines:
            tokenized =  line.split('\n')
            check_comment(tokenized[0])
