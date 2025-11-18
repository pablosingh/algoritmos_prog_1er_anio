from Menu import Menu
from GestorDePasajeros import GestorDePasajeros
from GestorDeVuelos import GestorDeVuelos
from GestorDeReservas import GestorDeReservas

def main():
    gestor_de_pasajeros = GestorDePasajeros()
    gestor_de_vuelos = GestorDeVuelos()
    gestor_de_reservas = GestorDeReservas(gestor_de_pasajeros, gestor_de_vuelos)

    opciones = [
        ("0- Salir", lambda: print("Saliendo...")),
        ("1- Gestor de Pasajeros", gestor_de_pasajeros.menu_pasajero_tupla),
        ("2- Gestor de Vuelos", gestor_de_vuelos.menu_vuelo_tupla),
        ("3- Gestor de Reservas", gestor_de_reservas.menu_reserva_tupla)
    ]
    mi_menu = Menu(opciones)
    mi_menu.seleccionar_func("=== Menu Principal ===")

main()