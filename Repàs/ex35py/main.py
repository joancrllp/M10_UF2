# main.py
from calclong import analizar_longitud_palabras

def main():
    
    frase_usuario = input("Introduce una frase: ")
    resultado = analizar_longitud_palabras(frase_usuario)
    for palabra, longitud in resultado.items():
           print(f"Palabra: {palabra}, Longitud: {longitud}")

if __name__ == "__main__":
    main()
