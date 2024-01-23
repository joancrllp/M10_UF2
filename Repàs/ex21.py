#Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista. 
#Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista. Mostrar per pantalla la llista.

#Exemple mostra per pantalla.
#Números de l’usuari:
#suma total:
#mitjana:

entrada_usuario = input("Escribe 10 números separados por espacios: ")
numeros_usuario = [int(num) for num in entrada_usuario.split()]

suma_total = sum(numeros_usuario)
media = suma_total / len(numeros_usuario)

numeros_usuario.append(suma_total)
numeros_usuario.append(media)

print("Números de l’usuari:", numeros_usuario)
print("Suma total:", suma_total)
print("Mitjana:", media)
