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

    def guardar_reservas(self) -> None:
        try:
            with open("reservas.bin", "wb") as archivo:
                pickle.dump(self.reservas, archivo)
        except FileNotFoundError:
            print("No se ha podido guardar el archivo")

    def cargar_reservas(self) -> None:
        try:
            with open("reservas.bin", "rb") as archivo:
                self.reservas = pickle.load(archivo)
        except FileNotFoundError:
            self.guardar_reservas()

    def agregar_reserva(self) -> None:
        print("\n=== Nueva Reserva ===")
        pasajero_encontrado: Pasajero | None = self.gestor_de_pasajeros.buscar_pasajero_por_dni()
        vuelos_filtrados: list[Vuelo] = self.gestor_de_vuelos.buscar_vuelo_por_origen_destino()
        self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados)
        if Herramientas.pedir_confirmacion("Desea Filtrar vuelos por Fecha?"):
            vuelos_filtrados_por_fecha = self.gestor_de_vuelos.filtrar_vuelos_por_fecha(vuelos_filtrados)
            self.gestor_de_vuelos.mostrar_vuelos(vuelos_filtrados_por_fecha)

        vuelo_encontrado: Vuelo | None = self.gestor_de_vuelos.buscar_vuelo_por_id()

        nueva_reserva: Reserva | None = Reserva(pasajero_encontrado, vuelo_encontrado, FechaHora())
        self.reservas.append(nueva_reserva)
        self.guardar_reservas()
        print("Reserva creada")

    def buscar_reserva_por_dni(self) -> Reserva | None:
        dni = input("Ingrese el DNI del pasajero para buscar su reserva: ")
        for reserva in self.reservas:
            if reserva.pasajero.dni == dni:
                return reserva
        return None

    def buscar_reserva(self) -> None:
        reserva = self.buscar_reserva_por_dni()
        if reserva:
            print(reserva)
        else:
            print("❌ No se encontró ninguna reserva para ese pasajero.")

    def eliminar_reserva(self) -> None:
        print("\n=== Eliminar Reserva ===")
        reserva = self.buscar_reserva_por_dni()
        if reserva:
            self.reservas.remove(reserva)
            self.guardar_reservas()
            print("✅ Reserva eliminada correctamente.")
        else:
            print("❌ No se encontró la reserva a eliminar.")

    def editar_reserva(self, gestor_vuelos: GestorDeVuelos) -> None:
        print("\n=== Editar Reserva ===")
        reserva = self.buscar_reserva_por_dni()
        if not reserva:
            print("❌ No se encontró la reserva a editar.")
            return

        print("Enter para dejar sin cambios.")
        nuevo_codigo = input(f"Código vuelo actual {reserva.vuelo.codigo}: ") or reserva.vuelo.codigo
        if nuevo_codigo != reserva.vuelo.codigo:
            nuevo_vuelo = gestor_vuelos.buscar_vuelo_por_codigo_manual(nuevo_codigo)
            if nuevo_vuelo:
                reserva.vuelo = nuevo_vuelo
            else:
                print("⚠️ No se encontró el vuelo, se mantiene el actual.")

        nueva_fecha = input(f"Fecha reserva actual {reserva.fecha_reserva}: ") or None
        if nueva_fecha:
            reserva.fecha_reserva = FechaHora(nueva_fecha)
        self.guardar_reservas()
        print("✅ Reserva actualizada.")

    def mostrar_reservas(self) -> None:
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        print("\n=== Lista de Reservas ===")
        for reserva in self.reservas:
            print(reserva)

    def mostrar_menu_reservas(self) -> None:
        print("\n=== MENÚ DE RESERVAS ===")
        print("0 - Salir")
        print("1 - Agregar Reserva")
        print("2 - Buscar Reserva")
        print("3 - Editar Reserva")
        print("4 - Eliminar Reserva")
        print("5 - Mostrar todas las Reservas")

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
                self.editar_reserva()
            elif opcion == 4:
                self.eliminar_reserva()
            elif opcion == 5:
                self.mostrar_reservas()
            else:
                print("❌ Opción inválida.")
