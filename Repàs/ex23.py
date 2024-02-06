import json

def crear_libro(titulo, portada, año, paginas):
    libro = {
        "title": titulo,
        "cover": portada,
        "year": año,
        "pages": paginas
    }
    return libro

def crear_y_guardar_json():
    libros = [
        crear_libro("Libro1", "Portada1", 2022, 300),
        crear_libro("Libro2", "Portada2", 2020, 250),
        crear_libro("Libro3", "Portada3", 2021, 200),
        crear_libro("Libro4", "Portada4", 2019, 350)
    ]

    d = {"book": libros}

    print(json.dumps(d, indent=2))

    with open("libros.json", "w") as archivo:
        json.dump(d, archivo, indent=2)

crear_y_guardar_json()
