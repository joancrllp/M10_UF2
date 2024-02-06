ftotal = input('Introdueix el preu de tot el carrito: ')

print(amb_iva(ftotal, iva))

def amb_iva(ftotal, iva = 21):
    ftotal = ftotal * iva   
    return ftotal 
# S'esta multiplicant ftotal per iva pero hauría d'estar sumant el percentatge de l'IVA al total, ja que com esta ara s'estaria
#multiplicant el preu del carrito per l'IVA. 