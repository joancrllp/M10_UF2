n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    for j in range(j, 1, -1):
        print(j, end=" ")
    print("")

#La variable j no està inicialitzada abans del bucle, el que provoca una excepció NameError. En el segon bucle s'ha de cambiar 
#la j per i, el 1 per un 0 i el -1 per un -2 per a que funcioni correctament
    
n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

    