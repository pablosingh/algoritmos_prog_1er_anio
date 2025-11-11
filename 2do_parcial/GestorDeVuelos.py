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

    def pedir_ciudad_valida(self, mensaje: str) -> str:
        while True:
            print(mensaje)
            self.mostrar_menu_ciudades()
            indice_de_ciudad = Herramientas().pedir_entero("Ingrese el nro de la Ciudad") - 1
            if indice_de_ciudad >= 0 and indice_de_ciudad < len(self.ciudades):
                return self.ciudades[indice_de_ciudad]
            else:
                print("El nro de la ciudad es invalido")

    def agregar_vuelo(self) -> None:
        print("=== Agregar Nuevo Vuelo ===")
        origen = self.pedir_ciudad_valida("Origen: ")
        destino = self.pedir_ciudad_valida("Destino: ")
        fecha_salida = FechaHora.pedir_fecha_hora_valida("Fecha Salida: ")
        fecha_llegada = FechaHora.pedir_fecha_hora_valida("Fecha Llegada: ")
        vuelo = Vuelo(self.calcular_id(), origen, destino, fecha_salida, fecha_llegada)
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
            if Herramientas.pedir_confirmacion(f"Editar Origen actual: {vuelo_a_editar.origen} "):
                nuevo_origen = self.pedir_ciudad_valida(f"Nuevo origen: ")
                vuelo_a_editar.origen = nuevo_origen
            if Herramientas.pedir_confirmacion(f"Editar Destino actual: {vuelo_a_editar.destino} "):
                nuevo_destino = self.pedir_ciudad_valida(f"Nuevo destino: ")
                vuelo_a_editar.destino = nuevo_destino
            if Herramientas.pedir_confirmacion(f"Editar Fecha Salida actual: {vuelo_a_editar.fecha_salida} "):
                nueva_fecha_salida = FechaHora.pedir_fecha_hora_valida("Nueva Fecha Salida: ")
                vuelo_a_editar.fecha_salida = nueva_fecha_salida
            if Herramientas.pedir_confirmacion(f"Editar Fecha Llegada actual: {vuelo_a_editar.fecha_salida} "):
                nueva_fecha_llegada = FechaHora.pedir_fecha_hora_valida("Nueva Fecha Llegada: ")
                vuelo_a_editar.fecha_llegada = nueva_fecha_llegada
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
