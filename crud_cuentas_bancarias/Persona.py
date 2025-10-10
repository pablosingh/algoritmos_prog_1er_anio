from Fecha import Fecha

class Persona:
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: Fecha, cuil: str, dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.cuil = cuil
        self.dni = dni

    def __str__(self) -> str:
        return f"CUIL: {self.cuil} \t| {self.nombre} \t| {self.apellido} \t| {self.fecha_nacimiento}"

    def pedir_fecha_nac_valida(self):
        while True:
            fecha_str = input("Ingresá una fecha (dd/mm/aaaa): ")
            try:
                partes = fecha_str.split("/")
                if len(partes) != 3:
                    raise ValueError("Formato incorrecto")

                # Conversión manual sin map()
                dia = int(partes[0])
                mes = int(partes[1])
                anio = int(partes[2])

                # Validaciones básicas
                if mes < 1 or mes > 12:
                    raise ValueError("Mes inválido")

                # Días por mes
                dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                # Año bisiesto
                if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                    dias_por_mes[1] = 29

                if dia < 1 or dia > dias_por_mes[mes - 1]:
                    raise ValueError("Día inválido")

                print(f"Fecha válida: {dia:02d}/{mes:02d}/{anio}")
                return f"{dia:02d}/{mes:02d}/{anio}"

            except ValueError as e:
                print("Error:", e)
                print("Usá el formato dd/mm/aaaa (por ejemplo, 05/10/2025).")
