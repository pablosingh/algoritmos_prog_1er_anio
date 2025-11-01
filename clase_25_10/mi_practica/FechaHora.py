from datetime import datetime
import re

class FechaHora:
    def __init__(self, fecha_hora_str: str = None):
        if not fecha_hora_str:
            ahora = datetime.now()
            self.dia = ahora.day
            self.mes = ahora.month
            self.anio = ahora.year
            self.hora = ahora.hour
            self.minuto = ahora.minute
        else:
            if not self.es_fecha_hora_valida(fecha_hora_str):
                raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")

            fecha_str, hora_str = fecha_hora_str.strip().split(" ")
            partes_fecha = fecha_str.split("/")
            partes_hora = hora_str.split(":")

            self.dia = int(partes_fecha[0])
            self.mes = int(partes_fecha[1])
            self.anio = int(partes_fecha[2])
            self.hora = int(partes_hora[0])
            self.minuto = int(partes_hora[1])

    def es_fecha_hora_valida(self, fecha_hora: str) -> bool:
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01][0-9]|2[0-3]):([0-5][0-9])$'
        return re.match(patron, fecha_hora) is not None

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}"