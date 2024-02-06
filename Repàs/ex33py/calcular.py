
def calcular_total_compra(llista_compra, iva):
    total_sin_descuento = sum(llista_compra.keys())
    
    print("Detalles de la compra:")
    for i, (preu, descompte) in enumerate(llista_compra.items(), start=1):
        preu_con_descuento = preu - (preu * descompte / 100)
        preu_con_iva = preu_con_descuento + (preu_con_descuento * (iva / 100))
        
        print(f"Producte {i}: {preu_con_iva:.2f} (Descompte: {preu_con_descuento:.2f}, IVA: {preu_con_iva - preu_con_descuento:.2f})")
