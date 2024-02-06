
def calcular_total_factura(quantitat_sense_iva, iva):
    if iva not in [4, 10, 21]:
        iva = 21  

    total = quantitat_sense_iva + (quantitat_sense_iva * (iva / 100))
    
    return total, quantitat_sense_iva, (total - quantitat_sense_iva)
