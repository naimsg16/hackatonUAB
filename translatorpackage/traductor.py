from deep_translator import GoogleTranslator

#import detectlanguage

#detectlanguage.configuration.api_key = "YOUR API KEY"
#languages = detectlanguage.languages()
#ESTE PROGRAMA LEE Y ECRIBE A LA INVERSA UNA PALABRA Y FRASE DE UN FICHERO

if __name__ == '__main__':
 #EL PROGRAMA TRADUCE ALGO DENTRO DE UN FICHERO

    with open("output.txt","r") as file:
        text = file.read()
        traductor = GoogleTranslator(source='auto', target='es') #for 
        print(traductor.translate(text))

   
 #EL PROGRAMA TRADUCIR PALABRA YA INSERTADA
"""
    palabra = "Dog" #no agafa la primera mayus en frase pero en paraula si
    traductor = GoogleTranslator(source='en', target='es')
    print(traductor.translate(palabra))
 """