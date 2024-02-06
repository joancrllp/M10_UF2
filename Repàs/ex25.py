import json

class Vehiculo:
    def __init__(self, marca, modelo, year, color, tipo_combustible, kilometraje):
        self._marca = marca
        self._modelo = modelo
        self._year = year
        self._color = color
        self._tipo_combustible = tipo_combustible
        self._kilometraje = kilometraje

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_year(self):
        return self._year

    def get_color(self):
        return self._color

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def get_kilometraje(self):
        return self._kilometraje

    
    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_year(self, year):
        self._year = year

    def set_color(self, color):
        self._color = color

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def set_kilometraje(self, kilometraje):
        self._kilometraje = kilometraje

    def partes(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Año: {self._year}")
        print(f"Color: {self._color}")
        print(f"Tipo de Combustible: {self._tipo_combustible}")
        print(f"Kilometraje: {self._kilometraje}")

    def to_dict(self):
        return {
            "marca": self._marca,
            "modelo": self._modelo,
            "year": self._year,
            "color": self._color,
            "tipo_combustible": self._tipo_combustible,
            "kilometraje": self._kilometraje
        }


if __name__ == "__main__":
    mi_coche = Vehiculo(marca="Toyota", modelo="Supra", year=2000, color="Azul", tipo_combustible="Gasolina", kilometraje=15000)

    mi_coche.partes()

    objeto_json = mi_coche.to_dict()
    print("\nObjeto en formato JSON:")
    print(json.dumps(objeto_json, indent=2))
