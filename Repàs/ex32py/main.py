
from calcular import calcular_cuadrados

def main():
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    cuadrados = calcular_cuadrados(lista_numeros)
    
    print("Lista original:", lista_numeros)
    print("Lista de cuadrados:", cuadrados)

if __name__ == "__main__":
    main()
