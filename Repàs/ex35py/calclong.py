def analizar_longitud_palabras(frase):
    palabras = frase.split()
    resultado = {palabra: len(palabra) for palabra in palabras}
    return resultado
