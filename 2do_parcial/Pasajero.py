
class Pasajero:
    def __init__(self, nombre: str, dni: str, nacionalidad: str ) :
        self.nombre = nombre
        self.dni = dni
        self.nacionalidad = nacionalidad

    def __str__(self) -> str:
        return f"{self.dni}\t|{self.nombre} \t|Nac: {self.nacionalidad}"
