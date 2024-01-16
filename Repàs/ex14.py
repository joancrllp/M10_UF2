
entrada_usuario = input("Introdueix 10 números separats per espais: ")

numeros = [int(x) for x in entrada_usuario.split()]

if len(numeros) == 10:
    tupla_ordenada = tuple(sorted(numeros))

    print("Tupla ordenada de manera ascendente:", tupla_ordenada)

