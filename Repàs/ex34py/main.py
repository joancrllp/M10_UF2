# main.py
from calcular import calcular_quadrat, aplicar_funcio_a_llista

def main():
    llista_original = [1, 2, 3, 4, 5]

        
    nova_llista = aplicar_funcio_a_llista(calcular_quadrat, llista_original)

        
    print("Lista original:", llista_original)
    print("Nueva lista con cuadrados:", nova_llista)


if __name__ == "__main__":
    main()
