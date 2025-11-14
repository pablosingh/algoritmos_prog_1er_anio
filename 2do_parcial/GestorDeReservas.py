import pickle
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

    def mostrar_menu_reservas(self) -> None:
        print("===============================================================================")
        print("=== MENÚ DE RESERVAS ===")
        print("\t0 - Salir")
        print("\t1 - Agregar Reserva")
        print("\t2 - Buscar Reserva por ID")
        print("\t3 - Buscar Reservas por DNI")
        print("\t4 - Editar Reserva")
        print("\t5 - Eliminar Reserva por ID")
        print("\t6 - Mostrar todas las Reservas")
        print("\t7 - Mostrar reservas por Vuelo")

    def menu_reservas(self, gestor_pasajeros: GestorDePasajeros, gestor_vuelos: GestorDeVuelos) -> None:
        while True:
            self.mostrar_menu_reservas()
            opcion = Herramientas.pedir_entero("Opción: ")
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_reserva()
            elif opcion == 2:
                self.buscar_reserva()
            elif opcion == 3:
                self.buscar_reserva_por_pasajero()
            elif opcion == 4:
                self.mostrar_reservas()
                self.editar_reserva()
            elif opcion == 5:
                self.mostrar_reservas()
                self.eliminar_reserva()
            elif opcion == 6:
                self.mostrar_reservas()
            elif opcion == 7:
                self.gestor_de_vuelos.mostrar_vuelos()
                self.mostrar_reservas_por_vuelo()
            else:
                print("Opción inválida.")
