#Crear una funció que retorni un XML (crear arxiu .xml i mostrar per consola l’XML). 
#La funció ha de crear l’XML, crear les etiquetes i inserir text segons les següents especificacions:
#Un root de nom students.
#Cinc childs (del root) amb nom student.
#Cada child student ha de tindre 4 subchilds:
 #name
 #surname
 #email
 #dni
#Ha d’haver-hi un atribut (amb nom i valor) a dintre de cada element child “student”.
#El text de cada etiqueta serà de la vostra elecció.

import xml.etree.ElementTree as ET

def crear_xml():
    root = ET.Element("students")

    for i in range(1, 6):
        student = ET.SubElement(root, "student")
        student.set("id", str(i)) 
        name = ET.SubElement(student, "name")
        name.text = f"Nombre{i}"

        surname = ET.SubElement(student, "surname")
        surname.text = f"Apellido{i}"

        email = ET.SubElement(student, "email")
        email.text = f"email{i}@example.com"

        dni = ET.SubElement(student, "dni")
        dni.text = f"DNI{i}"

    tree = ET.ElementTree(root)

    tree.write("students.xml")

    print(ET.tostring(root, encoding="utf-8").decode("utf-8"))

crear_xml()
