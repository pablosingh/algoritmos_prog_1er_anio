from Menu import Menu
from Herramientas import Herramientas
from Reserva import Reserva
from FechaHora import FechaHora
from Pasajero import Pasajero
from GestorDePasajeros import GestorDePasajeros
from Vuelo import Vuelo
from GestorDeVuelos import GestorDeVuelos

class GestorDeReservas:
    def __init__(self, gestor_de_pasajeros: GestorDePasajeros, gestor_de_vuelos: GestorDeVuelos):
        self.reservas: list[Reserva] = []
        self.gestor_de_pasajeros = gestor_de_pasajeros
        self.gestor_de_vuelos = gestor_de_vuelos
        self.cargar_reservas()

    def calcular_id(self) -> int:
        if len(self.reservas) == 0:
            return 1
        else:
            return self.reservas[len(self.reservas) - 1].id + 1

    def guardar_reservas(self) -> None:
        Herramientas.guardar_archivo_bin("reservas.bin", self.reservas)

    def cargar_reservas(self) -> None:
        self.reservas = Herramientas.cargar_archivo_bin("reservas.bin")

    def agregar_reserva(self) -> None:
        print("\n=== Nueva Reserva ===")
        pasajero_encontrado: Pasajero | None = self.gestor_de_pasajeros.buscar_pasajero_por_dni()
        if not pasajero_encontrado:
            print("No se encontro el pasajero")
            return None
        print(pasajero_encontrado)

        vuelos_filtrados: list[Vuelo] = self.gestor_de_vuelos.buscar_vuelo_por_origen_destino()
        if not vuelos_filtrados:
            print("No se encontraron vuelos disponibles")
            return None
        self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados)

        if Herramientas.pedir_confirmacion("Desea Filtrar vuelos por Fecha?"):
            vuelos_filtrados_por_fecha = self.gestor_de_vuelos.filtrar_vuelos_por_fecha(vuelos_filtrados)
            if not vuelos_filtrados_por_fecha:
                print("No se encontraron vuelos disponibles")
                return None
            self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados_por_fecha)

        vuelo_encontrado: Vuelo | None = self.gestor_de_vuelos.buscar_vuelo_por_id()
        if not vuelo_encontrado:
            print("No se encontro el vuelo")
            return None

        nueva_reserva: Reserva | None = Reserva(self.calcular_id(), pasajero_encontrado, vuelo_encontrado, FechaHora())
        self.reservas.append(nueva_reserva)
        self.guardar_reservas()
        print("Reserva creada")

    def mostrar_reservas_filtradas(self, reservas_filtradas: list[Reserva] | None) -> None:
        if reservas_filtradas is None or len(reservas_filtradas) == 0:
            print("No hay reservas...")
        else:
            for reserva in reservas_filtradas:
                print(reserva)

    def buscar_reserva_por_id(self)-> Reserva | None:
        id = Herramientas.pedir_entero("Ingrese el Id de la Reserva : ")
        for reserva in self.reservas:
            if reserva.id == id:
                return reserva
        return None

    def buscar_reserva(self)->None:
        reserva = self.buscar_reserva_por_id()
        if reserva:
            print(reserva)
        else:
            print("No se Encontro la Reserva")

    def eliminar_reserva(self) -> None:
        self.mostrar_reservas()
        print("=== Eliminar Reserva ===")
        reserva_a_eliminar = self.buscar_reserva_por_id()
        if reserva_a_eliminar:
            self.reservas.remove(reserva_a_eliminar)
            self.guardar_reservas()
            print("Reserva eliminada correctamente.\n")
        else:
            print("Error - No se encontró la reserva.\n")

#####################################################################
    def buscar_reserva_por_dni(self) -> list[Reserva] | None:
        reservas_para_retornar: list[Reserva] = []
        dni = self.gestor_de_pasajeros.pide_dni_valido_str("Ingrese el DNI del pasajero para buscar su reserva: ")
        for reserva in self.reservas:
            if reserva.pasajero.dni == dni:
                reservas_para_retornar.append(reserva)
        return reservas_para_retornar

    def buscar_reserva_por_pasajero(self) -> None:
        reservas = self.buscar_reserva_por_dni()
        self.mostrar_reservas_filtradas(reservas)

#####################################################################
    def editar_reserva(self) -> None:
        self.mostrar_reservas()
        print("\n=== Editar Reserva ===")
        reserva_a_editar = self.buscar_reserva_por_id()
        if not reserva_a_editar:
            print("No se encontro la reserva.")
            return None
        if Herramientas.pedir_confirmacion("Editar Pasajero? "):
            nuevo_pasajero = self.gestor_de_pasajeros.buscar_pasajero_por_dni()
            if nuevo_pasajero:
                reserva_a_editar.pasajero = nuevo_pasajero
            else:
                print("No se encontro el Pasajero.")
                return None
        if Herramientas.pedir_confirmacion("Editar Vuelo? "):
            vuelos_filtrados: list[Vuelo] = self.gestor_de_vuelos.buscar_vuelo_por_origen_destino()
            if vuelos_filtrados:
                self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados)
            else:
                print("No se encontro el Vuelo.")
                return None
            if Herramientas.pedir_confirmacion("Desea Filtrar vuelos por Fecha?"):
                vuelos_filtrados_por_fecha = self.gestor_de_vuelos.filtrar_vuelos_por_fecha(vuelos_filtrados)
                self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados_por_fecha)

            nuevo_vuelo: Vuelo | None = self.gestor_de_vuelos.buscar_vuelo_por_id()
            if nuevo_vuelo:
                reserva_a_editar.vuelo = nuevo_vuelo
        reserva_a_editar.fecha_reserva = FechaHora()
        self.guardar_reservas()
        print("Reserva actualizada.")

###################################################################
    def filtrar_reservas_por_id_vuelo(self, id: int)-> list[Reserva]:
        reservas_para_retornar: list[Reserva] = []
        for reserva in self.reservas:
            if reserva.vuelo.id == id:
                reservas_para_retornar.append(reserva)
        return reservas_para_retornar

    def mostrar_reservas_por_vuelo(self) -> None:
        self.gestor_de_vuelos.mostrar_vuelos()
        vuelo = self.gestor_de_vuelos.buscar_vuelo_por_id()
        if not vuelo:
            print("No se encontro el Vuelo.")
            return None
        reservas_por_id_vuelo = self.filtrar_reservas_por_id_vuelo(vuelo.id)
        if not reservas_por_id_vuelo:
            print("No se encontro el Vuelo.")
            return None
        self.mostrar_reservas_filtradas(reservas_por_id_vuelo)

    def mostrar_reservas(self) -> None:
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        print("\n=== Lista de Reservas ===")
        for reserva in self.reservas:
            print(reserva)

    def menu_reserva_tupla(self) -> None:
        mensaje = "===============================================================================\n"
        mensaje += "=== MENU DE RESERVAS ==="
        opciones = [
            ("\t0 - Salir", lambda: print("Saliendo...")),
            ("\t1 - Agregar Reserva", self.agregar_reserva),
            ("\t2 - Buscar Reserva por ID", self.buscar_reserva),
            ("\t3 - Buscar Reservas por DNI", self.buscar_reserva_por_pasajero),
            ("\t4 - Editar Reserva", self.editar_reserva),
            ("\t5 - Eliminar Reserva por ID", self.eliminar_reserva),
            ("\t6 - Mostrar todas las Reservas", self.mostrar_reservas),
            ("\t7 - Mostrar reservas por Vuelo", self.mostrar_reservas_por_vuelo)
        ]

        menu_reserva = Menu(opciones)
        menu_reserva.seleccionar_func(mensaje)