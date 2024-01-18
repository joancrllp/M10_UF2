#Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i
#mostrar per pantalla quantes vegades apareix cada lletra.
# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i
# mostrar per pantalla quantes vegades apareix cada lletra.
# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i
# mostrar per pantalla quantes vegades apareix cada lletra.

paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

frase_combinada = paraula1 + " " + paraula2

contador = {}

for lletra in frase_combinada:
    if lletra not in contador:
        contador[lletra] = 0
    
    contador[lletra] += 1

print("Freqüència de cada lletra:")
for lletra, x in contador.items():
    print(lletra,":",x," vegades")
