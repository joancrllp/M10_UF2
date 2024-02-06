
from generar import generar_numero_aleatorio

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
        
    numero_aleatorio = generar_numero_aleatorio(num1, num2)
        
    print(f"Número aleatorio entre {num1} y {num2}: {numero_aleatorio}")

if __name__ == "__main__":
    main()
