contactes = {'Roger':678232311, 'Oriol':566879326}

def elimina(contactes, user):
    del contactes[user]
    return contactes[user]

print(elimina(contactes, 'Pablo'))
#Quan intentas  eliminar un user que no existeix en el diccionari dona un KeyError, s'hauría d'afegir un if per a verificar que 
#l'user esta en el diccionari

contactes = {'Roger': 678232311, 'Oriol': 566879326}

def elimina(contactes, user):
    if user in contactes:
        del contactes[user]
        return "Contacte eliminat"
    else:
        return "El contacte no existeix"

print(elimina(contactes, 'Pablo'))