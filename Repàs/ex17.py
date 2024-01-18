#Igual que l’anterior però a la tupla afegir la frase sense els caràcters 
#repetits i mostrar el contingut de la tupla. Exemple: Usuari indica la 
#paula caracteristica. Es mostra per pantalla carteis.

frase=[]

frase_usuario = input("Introdueix una frase: ")
for i in frase_usuario:
    if i not in frase and i !=' ':
        frase.append(i)
        tupla = tuple(frase)
print("Contingut de la tupla:", tupla)
