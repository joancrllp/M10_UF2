#Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat. 
#S’haura de demanar a l’usuari que posi contactes (noms i edats).
# Si algun nom es repeteix no s’fageirà al diccionari 
#(indicant-ho a l’usuari). Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

dicci = {}
print("Dime un nombre y su edad o escribe 'salir' para acabar el programa: ")

while True:
    nombre = input("Dime el nombre o escribe 'salir' para acabar el programa: ")
    edad = input("Dime la edad o escribe 'salir' para acabar el programa: ")

    if nombre == "salir" or edad == "salir":
        break

    if nombre in dicci:
        print("El nombre", nombre," ya está en el diccionario. Introduce otro nombre.")
    else:
        dicci[nombre] = edad

print(dicci)
