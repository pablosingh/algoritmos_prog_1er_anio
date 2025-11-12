from FechaHora import FechaHora
from Vuelo import Vuelo
from Pasajero import Pasajero

class Reserva:
    def __init__(self, pasajero: Pasajero, vuelo: Vuelo, fecha_reserva: FechaHora):
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva

    def __str__(self) -> str:
        return f"Reserva: {self.pasajero.__str__()}\t|{self.vuelo.__str__()} \t| {self.fecha_reserva.__str__()} \t|{self.fecha_llegada.__str__()}"

