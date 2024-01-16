
numero = int(input("Introdueix un número de l'1 al 10: "))

if 1 <= numero <= 10:
   
    print("Taula de multiplicar de", numero)
    for i in range(1, 11):
        resultat = numero * i
        print(resultat)

    
else:
    print("Número no vàlid")
