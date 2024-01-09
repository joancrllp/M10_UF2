
e = input("Introdueix un valor en euros: ")
i = input("Introduiex l'IVA que vols aplicar, el 4%, 10% o 21%: ")
ef = float(e)
iff = float(i)

if i == "4" or i == "4%":
    iva4 = ef / 100 * 4
    print("El valor que ha introduit l'usuari es,", e, "l'IVA que ha demana l'usuari es,", i, "i el valor escollit per l'usuari amb l'IVA afegit es", iva4)
elif i == "10" or i == "10%":
    iva10 = ef / 100 * 10
    print("El valor que ha introduit l'usuari es,", e, "l'IVA que ha demana l'usuari es,", i, "i el valor escollit per l'usuari amb l'IVA afegit es", iva10)
elif i == "21" or i == "21%":
    iva21 = ef / 100 * 21
    print("El valor que ha introduit l'usuari es,", e, "l'IVA que ha demana l'usuari es,", i, "i el valor escollit per l'usuari amb l'IVA afegit es", iva21)
else:
    print("L'IVA introduït no és vàlid. Per favor, introdueix 4%, 10% o 21%.")

 	 
