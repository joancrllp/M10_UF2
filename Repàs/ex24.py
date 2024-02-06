import json

def leer_y_mostrar_json():
    
    with open("libros.json", "r") as archivo:
        data = json.load(archivo)

    
    print(json.dumps(data, indent=2))
    
   
leer_y_mostrar_json()
