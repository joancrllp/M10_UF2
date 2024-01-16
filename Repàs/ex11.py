#Demanar a l’usuari un nùmero entre 10 i 100. Posar els números a una tupla 
#desde 1 fins al número indicat per l’usuari. Exemple: usuari indica 34, 
#es crea una tupla  i es mostra per pantalla els 
#números de l’1 al 34 (imprimint la tupla).

tupla=()
y = list(tupla)
pregunta = int(input("Introduiex un numero del 10 al 100"))

for i in range(1,pregunta+1):
    y.append(i)

tupla = tuple(y)
print(tupla)