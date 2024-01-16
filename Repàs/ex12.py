#Crear una tupla amb els mesos de l’any. Demanar a l’usuari que posi 
#un número entre 0 i 12 i mostrar per pantalla el mes corresponent 
#al número indicat per l’usuari. El programa finalitza només quan l’usuari 
#posa 0.
# Crear una tupla con los meses del año
meses = ('Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre')

while True:
   
    numero = int(input("Introdueix un número entre 0 i 12 o 0 per sortir "))


    if numero == 0:
       
        break

    
    elif 0 < numero <= 12:
        mes = meses[numero - 1]
        print(mes)
    else:
        
        print("Número no vàlid. ")