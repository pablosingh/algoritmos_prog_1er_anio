from Fecha import Fecha

class Cliente:
    def __init__(self, nombre: str, dni: int, fecha_nacimiento: Fecha):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"DNI: {self.dni} | {self.nombre} | Nac: {self.fecha_nacimiento}"
