from calcular import calcular_total_compra

def main():
   
    llista_compra = {100: 10, 250: 5, 1500: 30}

    iva = float(input("Introduce el porcentaje de IVA a aplicar (ejemplo: 21): "))

    calcular_total_compra(llista_compra, iva)

    
if __name__ == "__main__":
    main()
