#Demanar a l’usuari una frase. El programa eliminarà els espais i 
#s'afegirà a una tupla.
#Mostrar per pantalla el contingut de la tupla.
frase=[]

frase_usuario = input("Introdueix una frase: ")
for i in frase_usuario:
    if i != ' ':
        frase.append(i)
        tupla = tuple(frase)
print("Contingut de la tupla:", tupla)
