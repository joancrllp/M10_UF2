
from calcular1 import calcular_total_factura

def main():
   
    quantitat_sense_iva = float(input("Introduce la cantidad sin IVA: "))
    iva = int(input("Introduce el IVA (4%, 10% o 21%): "))
        
    total, subtotal, iva_total = calcular_total_factura(quantitat_sense_iva, iva)
        
    print(f"Subtotal: {subtotal} €")
    print(f"IVA ({iva}%): {iva_total} €")
    print(f"Total: {total} €")

   

if __name__ == "__main__":
    main()
