import pickle

from Cliente import Cliente
from Fecha import Fecha
from Herramientas import Herramientas

class GestorDeClientes:
    def __init__(self):
        self.clientes: list[Cliente] = []

    def agregar_cliente(self)-> None:
        nombre = input("Ingrese el Nombre y/o Apellido : ")
        dni = int(input("Ingrese el DNI : "))
        fecha_nacimiento_str = Herramientas.pedir_fecha_valida()
        self.clientes.append(Cliente(nombre, dni, Fecha(fecha_nacimiento_str)))
        self.guardar_clientes()

    def mostrar_clientes(self)-> None:
        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente_por_dni(self) -> Cliente | None:
        dni = Herramientas.pedir_entero("Ingrese el DNI a buscar: ")
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        print("No se encontro el Cliente")
        return None

    def borrar_cliente_por_dni(self) -> None:
        cliente = self.buscar_cliente_por_dni()
        if cliente:
            self.clientes.remove(cliente)
            self.guardar_clientes()
        else:
            print("No se encontro el Cliente a Borrar")

    def mostrar_menu_editar(self, cliente: Cliente)->None:
        print("\tMenu de Edición =============================")
        print(f"\t\tDNI: {cliente.dni} | {cliente.nombre} | {cliente.fecha_nacimiento}")
        print("\t\t1. Editar Nombre/Apellido")
        print("\t\t2. Editar DNI")
        print("\t\t3. Editar Fecha de Nacimiento")
        print("\t\t4. Guardar y Salir - Volver")

    def editar_cliente(self)->None:
        cliente = self.buscar_cliente_por_dni()
        opciones = ["1", "2", "3", "4"]
        if cliente:
            while True:
                self.mostrar_menu_editar(cliente)
                opcion = input("Opcion : ")
                if opcion in opciones:
                    if opcion == "1":
                        nombre = input("Ingrese el Nuevo Nombre/Apellido : ")
                        cliente.nombre = nombre
                    elif opcion == "2":
                        dni = Herramientas.pedir_entero("Ingrese el Nuevo DNI : ")
                        cliente.dni = dni
                    elif opcion == "3":
                        fecha_nac = Herramientas.pedir_fecha_valida()
                        cliente.fecha_nacimiento = fecha_nac
                    elif opcion == "4":
                        print("Cliente Editado - Volviendo")
                        self.guardar_clientes()
                        break
                else:
                    print("Opcion invalida")
        else:
            print("Cliente no encontrado")

    def guardar_clientes(self)-> None:
        with open("clientes.bin", "wb") as archivo:
            pickle.dump(self.clientes, archivo)

    def cargar_clientes(self)-> None:
        with open("clientes.bin", "rb") as archivo:
            self.clientes = pickle.load(archivo)

    def mostrar_menu_clientes(self)-> None:
        print("========== MENU DE CLIENTES ===============")
        print("\t0- Volver - Salir")
        print("\t1- Agregar Cliente")
        print("\t2- Editar Cliente")
        print("\t3- Borrar Cliente")
        print("\t4- Listar todos los Clientes")

    def menu_clientes(self)-> None:
        opciones = ["0", "1", "2", "3", "4"]
        while True:
            self.mostrar_menu_clientes()
            opcion = input("\tOpcion : ")
            if opcion in opciones:
                if opcion == "0":
                    break
                elif opcion == "1":
                    self.agregar_cliente()
                elif opcion == "2":
                    self.editar_cliente()
                elif opcion == "3":
                    self.borrar_cliente_por_dni()
                elif opcion == "4":
                    self.mostrar_clientes()
            else:
                print("Opcion invalida")