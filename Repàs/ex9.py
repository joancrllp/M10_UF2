#Demanar a l’usuari que posi dues paraules. Al executar el programa, 
#mostrarà per pantalla les dues paraules amb els dos primers caràcters de cada paraula intercanviats. 
#Exemple: Quatre Camins passaria a Caatre Qumins.

paraula1=[]
paraula2=[]




paraulaa1 = input("Introdueix la paraula 1 ")
paraula1.append(paraulaa1)
paraulaa2 = input("Introdueix la paraula 2 ")
paraula2.append(paraulaa2)

novaparaulaa1=paraulaa1.replace(paraulaa1[0],paraulaa2[0])
novaparaulaa1=novaparaulaa1.replace(paraulaa1[1],paraulaa2[1])
print(novaparaulaa1)

novaparaulaa2=paraulaa2.replace(paraulaa2[0],paraulaa1[0])
novaparaulaa2=novaparaulaa2.replace(paraulaa2[1],paraulaa1[1])
print(novaparaulaa2)




