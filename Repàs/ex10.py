import random
#Crear un arxiu on caldrà endevinar el número escollit pel programa 
#entre 1 i 100. Cada vegada que l’usuari hi posi un número, caldrà 
#indicar si és més petit o més gran fins que encerti i el missatge 
#haurà d’indicar que ha encertat. Indicar també el número d’intents.
x= random.randint(0, 100)
contador=0
while True:
    num=int(input("Introdueix un numero"))
    
    if num >x:
        print("El numero es més petit")
    elif num <x:
        print("El numero es més gran")
    elif num == x:
        print("Has acertat el numero en", contador, "intents")
        break
    contador+=1;
