import json

class User:
    def __init__(self, nom, cognom, edat, email, ciutat, telefon):
        self._nom = nom
        self._cognom = cognom
        self._edat = edat
        self._email = email
        self._ciutat = ciutat
        self._telefon = telefon

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def get_cognom(self):
        return self._cognom

    def set_cognom(self, cognom):
        self._cognom = cognom

    def get_edat(self):
        return self._edat

    def set_edat(self, edat):
        self._edat = edat

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_ciutat(self):
        return self._ciutat

    def set_ciutat(self, ciutat):
        self._ciutat = ciutat

    def get_telefon(self):
        return self._telefon

    def set_telefon(self, telefon):
        self._telefon = telefon

    def salutacio(self):
        print(f"Nom: {self._nom}")
        print(f"Cognom: {self._cognom}")
        print(f"Edat: {self._edat}")
        print(f"Email: {self._email}")
        print(f"Ciutat: {self._ciutat}")
        print(f"Telefon: {self._telefon}")

    def to_dict(self):
        return {
            "nom": self._nom,
            "cognom": self._cognom,
            "edat": self._edat,
            "email": self._email,
            "ciutat": self._ciutat,
            "telefon": self._telefon
        }

if __name__ == "__main__":
    
    usuari = User(nom="Joan", cognom="Cruz", edat=20, email="joancruzlopez7@gmail.com", ciutat="Barcelona", telefon="655996870")

    usuari.salutacio()

    objeto_json = usuari.to_dict()
    print("\nObjecte en format JSON:")
    print(json.dumps(objeto_json, indent=2))
