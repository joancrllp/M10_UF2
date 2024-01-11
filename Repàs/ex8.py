#Demanar a l’usuari que posi entre 1 i 3 paraules. Al executar el programa, mostrarà la/es paraula/es indicada/es per l’usuari, 
#indicar quants caràcters té i indicar el primer, i l’últim caràcter.


num_paraules = int(input("Introdueix el nombre de paraules entre 1 i 3: "))


paraules = []
    
for i in range(num_paraules):
    paraula = input("Introdueix la paraula")
    paraules.append(paraula)
    
for paraula in paraules:
    print("La paraula",paraula,"té",len(paraula),"caracters,el primer caracter es", paraula[0]," i l'ultim",paraula[-1])
   
