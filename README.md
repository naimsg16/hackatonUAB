# Translator UAB the Hack
The **Translator UAB the Hack** is a pip library that provides methods to translate your Python code from one language to another, translating comments and variables.
### Installing
Just download it by typing in the command line:
```
pip install translator-uabthehack
```
### Running it on your code
Import the main method by using :
```
from translator_uabthehack.main import translate_code
```
And then run the method:
```
translate_code("input_file","language","output_file")
```
Where:
- ```input_file``` the name of the file that has to be translated (_i.e. myproject.py_)
- ```language``` the name of the language (in english) to which the program has to translate (see list down below)
* ```output_file``` the name of the file where the translated code will be stored (if it doesn't exist it will create it)

### List of languages
- Afrikaans
- Arabic
- Bulgarian
- Bengali
- Catalan
- Czech
- Welsh
- Danish
- German
- Greek
- English
- Spanish
- Estonian
- Persian (Farsi)
- Finnish
- French
- Gujarati
- Hebrew
- Hindi
- Croatian
- Hungarian
- Indonesian
- Italian
- Japanese
- Kannada
- Korean
- Lithuanian
- Latvian
- Macedonian
- Malayalam
- Marathi
- Dutch
- Dutch
- Norwegian
- Punjabi
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Slovenian
- Somali
- Albanian
- Swedish
- Swahili
- Tamil
- Telugu
- Thai
- Tagalog
- Turkish
- Ukrainian
- Urdu
- Vietnamese
- Chinese (Simplified)
- Chinese (Traditional)
### Errors
There are some sequences that can't be translated and / or interpreted by our translator, so follow these steps:
- Don't use the symbol "#" outside of the comment marker
- Don't use the word "import" in your code (it should be fine in the comments)
