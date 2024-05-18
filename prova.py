import random

randomN = random.randint(1, 10) #Generar un numero aleatori del 1 al 10
    
print("adivina el numero!!! o sino no tindras una Gemma gratis")
intents = 0 #Intents que has fer per adivinar
playerN = int(input("introdueix el numero: ")) #Llegeix el numero del usuari
intents +=1#Numero de intents

while playerN != randomN: #Bucle per tornar intentar si fallas, has perdut?
    print("torna a intentar") #Condicio si fallas
    playerN = int(input("introdueix el numero de nou: "))
    intents +=1 

if playerN == randomN: #Condició si has guanyat + acabar codi
    print("molt be has guanyat") #Has guanyat text
    print(intents)
