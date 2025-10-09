class Fecha:
    def __init__(self, fecha_str):
        fecha_nacimiento_split = fecha_str.split("/")
        self.dia = int(fecha_nacimiento_split[0])
        self.mes = int(fecha_nacimiento_split[1])
        self.anio = int(fecha_nacimiento_split[2])