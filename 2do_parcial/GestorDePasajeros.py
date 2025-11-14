import pickle
from Herramientas import Herramientas
from Pasajero import Pasajero

class GestorDePasajeros:
    def __init__(self):
        self.pasajeros: Pasajero = []
        self.cargar_pasajeros()

    def guardar_pasajeros(self) -> None:
        try:
            with open("pasajeros.bin", "wb") as archivo:
                pickle.dump(self.pasajeros, archivo)
        except FileNotFoundError:
            print("No se ha podido guardar el archivo")

    def cargar_pasajeros(self) -> None:
        try:
            with open("pasajeros.bin", "rb") as archivo:
                self.pasajeros = pickle.load(archivo)
        except FileNotFoundError:
            self.guardar_pasajeros()

    def pide_dni_valido_str(self, mensaje: str)->str:
        while True:
            if mensaje:
                print(mensaje)
            dni = input("DNI : ").strip()
            dni = dni.replace(".", "")
            if dni.isnumeric() and len(dni) > 6 and len(dni) < 9:
                if not self.es_dni_duplicado(dni):
                    return dni
                else:
                    print("DNI duplicado")
            else:
                print("Ingrese un DNI correcto.")

    def es_dni_duplicado(self, dni: str)->bool:
        for pasajero in self.pasajeros:
            if pasajero.dni == dni:
                return True
        return False

    def agregar_pasajero(self)->None:
        nombre = input("Ingrese el Nombre/Apellido del Pasajero : ")
        dni = self.pide_dni_valido_str()
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
            print("Enter para continuar")
            pasajero_a_editar.dni = self.pide_dni_valido_str(f"DNI {pasajero_a_editar.dni}| Nuevo DNI ")
            pasajero_a_editar.nombre = input(f"{pasajero_a_editar.nombre}| Nuevo Nombre: ") or pasajero_a_editar.nombre
            pasajero_a_editar.nacionalidad = input(f"{pasajero_a_editar.nacionalidad}| Nuevo Nacionalidad: ") or pasajero_a_editar.nacionalidad
            self.guardar_pasajeros()
        else:
            print("No se encontro el Pasajero.-")

    def mostrar_pasajeros(self)->None:
        for pasajero in self.pasajeros:
            print(pasajero)

    def mostrar_menu_pasajeros(self)->None:
        print("===============================================================================")
        print("=== MENU DE PASAJEROS ===")
        print("\t0 - Salir")
        print("\t1 - Agregar Pasajero")
        print("\t2 - Buscar Pasajero / Mostrar detalles de un Pasajero")
        print("\t3 - Editar Pasajero")
        print("\t4 - Eliminar Pasajero")
        print("\t5 - Mostrar todos los Pasajeros")

    def menu_pasajero(self)->None:
        while True:
            self.mostrar_menu_pasajeros()
            opcion = Herramientas.pedir_entero("Opcion: ")
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_pasajero()
            elif opcion == 2:
                self.buscar_pasajero()
            elif opcion == 3:
                self.editar_pasajero()
            elif opcion == 4:
                self.eliminar_pasajero_dni()
            elif opcion == 5:
                self.mostrar_pasajeros()
            else:
                print("Opcion Invalida")