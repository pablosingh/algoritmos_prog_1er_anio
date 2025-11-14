from FechaHora import FechaHora
from Vuelo import Vuelo
from Pasajero import Pasajero

class Reserva:
    def __init__(self, id: int, pasajero: Pasajero, vuelo: Vuelo, fecha_reserva: FechaHora):
        self.id = id
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva

    def __str__(self) -> str:
        return (f"ID Reserva: {self.id}\n "
                f"{self.pasajero.__str__()}\n "
                f"{self.vuelo.__str__()} \n "
                f"Creacion de Reserva: {self.fecha_reserva.__str__()}\n"
                f"---------------------------------")


