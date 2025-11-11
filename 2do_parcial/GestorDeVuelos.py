from Herramientas import Herramientas
from Vuelo import Vuelo
from FechaHora import FechaHora

class GestorDeVuelos:
    def __init__(self):
        self.vuelos: list[Vuelo] = []
        self.ciudades: list[str] = [
            "Buenos Aires",
            "Catamarca",
            "Chaco",
            "Chubut",
            "Córdoba",
            "Corrientes",
            "Entre Ríos",
            "Formosa",
            "Jujuy",
            "La Pampa",
            "La Rioja",
            "Mendoza",
            "Misiones",
            "Neuquén",
            "Río Negro",
            "Salta",
            "San Juan",
            "San Luis",
            "Santa Cruz",
            "Santa Fe",
            "Santiago del Estero",
            "Tierra del Fuego",
            "Tucumán"
        ]

    def calcular_id(self) -> int:
        if len(self.vuelos) == 0:
            return 1
        else:
            return self.vuelos[len(self.vuelos) - 1].id + 1

    def agregar_vuelo(self) -> None:
        print("=== Agregar Nuevo Vuelo ===")

        print("Ingrese el origen del vuelo: ")
        self.mostrar_menu_ciudades()
        indice_de_origen = Herramientas().pedir_entero("Ingrese el nro del Origen") - 1

        print("Ingrese el destino del vuelo: ")
        self.mostrar_menu_ciudades()
        indice_de_destino = Herramientas().pedir_entero("Ingrese el nro del Destino") - 1


        print("---- Fecha de salida ----")
        fecha_salida = FechaHora.pedir_fecha_hora_valida()

        print("---- Fecha de llegada ----")
        fecha_llegada = FechaHora.pedir_fecha_hora_valida()

        vuelo = Vuelo(self.calcular_id(), self.ciudades[indice_de_origen], self.ciudades[indice_de_destino], fecha_salida, fecha_llegada)
        self.vuelos.append(vuelo)
        print("Vuelo agregado correctamente.\n")

    def buscar_vuelo_por_origen_destino(self) -> Vuelo | None:
        origen = input("Ingrese el origen del vuelo: ")
        destino = input("Ingrese el destino del vuelo: ")

        for vuelo in self.vuelos:
            if vuelo.origen.lower() == origen.lower() and vuelo.destino.lower() == destino.lower():
                return vuelo
        return None

    def buscar_vuelo_por_id(self)-> Vuelo | None:
        id = Herramientas.pedir_entero("Ingrese el Id del Vuelo a buscar : ")
        for vuelo in self.vuelos:
            if vuelo.id == id:
                return vuelo
        return None

    def buscar_vuelo(self)->None:
        vuelo = self.buscar_vuelo_por_origen_destino()
        if vuelo:
            print(vuelo)
        else:
            print("No se Encontro el vuelo")

    def eliminar_vuelo(self) -> None:
        print("=== Eliminar Vuelo ===")
        vuelo_a_eliminar = self.buscar_vuelo_por_id()
        if vuelo_a_eliminar:
            self.vuelos.remove(vuelo_a_eliminar)
            print("Vuelo eliminado correctamente.\n")
        else:
            print("Error - No se encontró el vuelo.\n")

    def editar_vuelo(self) -> None:
        print("=== Editar Vuelo ===")
        vuelo_a_editar = self.buscar_vuelo_por_id()
        if vuelo_a_editar:
            print("Presione ENTER para mantener el valor actual.\n")
            nuevo_origen = input(f"Origen actual: {vuelo_a_editar.origen} | Nuevo origen: ") or vuelo_a_editar.origen
            nuevo_destino = input(f"Destino actual: {vuelo_a_editar.destino} | Nuevo destino: ") or vuelo_a_editar.destino

            print("---- Nueva Fecha de salida (Enter para mantener) ----")
            cambiar_salida = input("¿Desea cambiar la fecha de salida? (s/n): ").lower()
            if cambiar_salida.startswith("s"):
                vuelo_a_editar.fecha_salida = FechaHora.crear_desde_input()

            print("---- Nueva Fecha de llegada (Enter para mantener) ----")
            cambiar_llegada = input("¿Desea cambiar la fecha de llegada? (s/n): ").lower()
            if cambiar_llegada.startswith("s"):
                vuelo_a_editar.fecha_llegada = FechaHora.crear_desde_input()

            vuelo_a_editar.origen = nuevo_origen
            vuelo_a_editar.destino = nuevo_destino
            print("Vuelo actualizado correctamente.\n")
        else:
            print("No se encontró el vuelo a editar.\n")

    def mostrar_vuelos(self) -> None:
        print("=== Lista de Vuelos ===")
        if not self.vuelos:
            print("No hay vuelos registrados.\n")
        else:
            for vuelo in self.vuelos:
                print(vuelo)

    def mostrar_menu_vuelos(self) -> None:
        print("\n===== MENÚ GESTOR DE VUELOS =====")
        print("0 - Salir")
        print("1 - Agregar Vuelo")
        print("2 - Buscar Vuelo")
        print("3 - Editar Vuelo")
        print("4 - Eliminar Vuelo")
        print("5 - Mostrar todos los Vuelos")

    def mostrar_menu_ciudades(self) -> None:
        print("Ciudades Disponibles: ")
        for i in range(len(self.ciudades)):
            print(f"{i+1}- {self.ciudades[i]}")


    def menu_vuelos(self) -> None:
        while True:
            self.mostrar_menu_vuelos()
            opcion = Herramientas.pedir_entero("Opción: ")
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_vuelo()
            elif opcion == 2:
                self.buscar_vuelo()
            elif opcion == 3:
                self.editar_vuelo()
            elif opcion == 4:
                self.eliminar_vuelo()
            elif opcion == 5:
                self.mostrar_vuelos()
            else:
                print("Opción inválida, intente nuevamente.\n")
