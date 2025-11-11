from FechaHora import FechaHora

class Vuelo:
    def __init__(self, id: int, origen: str, destino: str, fecha_salida: FechaHora, fecha_llegada: FechaHora ):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada

    def __str__(self) -> str:
        return f"Vuelo: {self.origen}\t|{self.destino} \t| Salida: {self.fecha_salida.__str__()} \t|{self.fecha_llegada.__str__()}\n"
