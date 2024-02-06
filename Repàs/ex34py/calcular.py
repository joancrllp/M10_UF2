
def calcular_quadrat(numero):
    return numero ** 2

def aplicar_funcio_a_llista(funcio, llista):
    nova_llista = [funcio(element) for element in llista]
    return nova_llista
