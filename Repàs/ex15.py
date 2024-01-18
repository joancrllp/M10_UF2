
numeros = []
 
while True:
    entrada_usuario = input("Introdueix un número ") 
    if entrada_usuario=="0":
        break
   
    numero = int(entrada_usuario)
    tupla_ordenada = tuple(sorted(numeros))
    
    numeros.append(numero)
   
print("Tupla ordenada:", tupla_ordenada)