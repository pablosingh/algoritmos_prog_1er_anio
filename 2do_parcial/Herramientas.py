import re

class Herramientas:
    @staticmethod
    def pedir_entero(mensaje: str)-> int:
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Ingresá un numero entero. ")

    @staticmethod
    def pedir_float(mensaje: str)-> float:
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Ingresá un numero decimal. ")

    @staticmethod
    def pedir_fecha_valida()-> str:
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        while True:
            fecha = input("Ingrese la Fecha de Nacimiento (dd/mm/yyyy) : ")
            if re.match(patron, fecha):
                return fecha
            else:
                print("Formato invalido.")

    @staticmethod
    def pedir_confirmacion(mensaje: str) -> bool:
        while True:
            respuesta = input(f"{mensaje} (S/N) o (Enter = Si) : ").strip().lower()
            if not respuesta:
                return True

            if respuesta[0] == "s":
                return True
            elif respuesta[0] == "n":
                return False
            else:
                print("Opción inválida. Ingrese 'S' para Sí o 'N' para No.")