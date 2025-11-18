from Herramientas import Herramientas
from Pasajero import Pasajero
from Menu import Menu

class GestorDePasajeros:
    def __init__(self):
        self.pasajeros: Pasajero = []
        self.cargar_pasajeros()

    def guardar_pasajeros(self) -> None:
        Herramientas().guardar_archivo_bin("pasajeros.bin", self.pasajeros)
        return None

    def cargar_pasajeros(self) -> None:
        self.pasajeros = Herramientas.cargar_archivo_bin("pasajeros.bin")
        return None

    def pide_dni_valido_str(self, mensaje: str | None)->str:
        while True:
            if mensaje:
                print(mensaje)
            dni = input("DNI : ").strip()
            dni = dni.replace(".", "")
            if dni.isnumeric() and len(dni) > 6 and len(dni) < 9:
                return dni
            else:
                print("Ingrese un DNI correcto.")

    def es_dni_duplicado(self, dni: str)->bool:
        for pasajero in self.pasajeros:
            if pasajero.dni == dni:
                return True
        return False

    def agregar_pasajero(self)->None:
        nombre = input("Ingrese el Nombre/Apellido del Pasajero : ")
        dni = self.pide_dni_valido_str("")
        while self.es_dni_duplicado(dni):
            dni = self.pide_dni_valido_str("")
        nacionalidad = input("Ingrese la nacionalidad : ")

        self.pasajeros.append(Pasajero(nombre, dni, nacionalidad))
        self.guardar_pasajeros()

    def buscar_pasajero_por_dni(self)-> Pasajero | None:
        dni = self.pide_dni_valido_str("Ingrese el DNI a buscar : ")
        for pasajero in self.pasajeros:
            if pasajero.dni == dni:
                return pasajero
        return None

    def buscar_pasajero(self)->None:
        pasajero = self.buscar_pasajero_por_dni()
        if pasajero:
            print(pasajero)
        else:
            print("No se Encontro el pasajero")

    def eliminar_pasajero_dni(self)->None:
        print("Para Eliminar un Pasajero")
        pasajero_a_eliminar =  self.buscar_pasajero_por_dni()
        if pasajero_a_eliminar:
            self.pasajeros.remove(pasajero_a_eliminar)
            self.guardar_pasajeros()
        else:
            print("Error - No se encontro el Pasajero")

    def editar_pasajero(self)->None:
        print("Para Editar un Pasajero")
        pasajero_a_editar = self.buscar_pasajero_por_dni()
        if pasajero_a_editar:
            dni = self.pide_dni_valido_str(f"DNI {pasajero_a_editar.dni}| Nuevo DNI ")
            while self.es_dni_duplicado(dni):
                if pasajero_a_editar.dni == dni:
                    break
                print("DNI Duplicado")
                dni = self.pide_dni_valido_str(f"DNI {pasajero_a_editar.dni}| Nuevo DNI ")
            pasajero_a_editar.dni = dni
            print("Enter para continuar")
            pasajero_a_editar.nombre = input(f"{pasajero_a_editar.nombre}| Nuevo Nombre: ") or pasajero_a_editar.nombre
            pasajero_a_editar.nacionalidad = input(f"{pasajero_a_editar.nacionalidad}| Nuevo Nacionalidad: ") or pasajero_a_editar.nacionalidad
            self.guardar_pasajeros()
        else:
            print("No se encontro el Pasajero.-")

    def mostrar_pasajeros(self)->None:
        for pasajero in self.pasajeros:
            print(pasajero)

    def menu_pasajero_tupla(self)->None:
        mensaje = "===============================================================================\n"
        mensaje += "=== MENU DE PASAJEROS ==="
        opciones = [
            ("\t0 - Salir", lambda: print("Saliendo...")),
            ("\t1 - Agregar Pasajero", self.agregar_pasajero),
            ("\t2 - Buscar Pasajero / Mostrar detalles de un Pasajero", self.buscar_pasajero),
            ("\t3 - Editar Pasajero", self.editar_pasajero),
            ("\t4 - Eliminar Pasajero", self.eliminar_pasajero_dni),
            ("\t5 - Mostrar todos los Pasajeros", self.mostrar_pasajeros)
        ]

        menu_pasajeros = Menu(opciones)
        menu_pasajeros.seleccionar_func(mensaje)