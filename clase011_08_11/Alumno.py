class Alumno:
    def __init__(self, dni: int, nombre: str, email: str, carrera: str):
        self.dni = dni
        self.nombre = nombre
        self.email = email
        self.carrera = carrera

    def __str__(self):
        return f"DNI: {self.dni}| {self.nombre}| {self.email}| {self.carrera}\n"