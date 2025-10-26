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

