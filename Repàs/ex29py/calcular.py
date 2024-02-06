
def mostrar_numeros_entre_y_suma(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Números enteros entre {num1} y {num2}:")
    suma_numeros = 0

    for i in range(int(num1), int(num2) + 1):
        print(i)
        suma_numeros += i

    print(f"\nSuma de los números enteros: {suma_numeros}")
