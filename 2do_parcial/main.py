from Menu import Menu
from Herramientas import Herramientas
from GestorDePasajeros import GestorDePasajeros
from GestorDeVuelos import GestorDeVuelos
from GestorDeReservas import GestorDeReservas

def mostrar_menu_principal():
    print("=== Menu Principal ===")
    print("0- Salir")
    print("1- Gestor de Pasajeros")
    print("2- Gestor de Vuelos")
    print("3- Gestor de Reservas")

def menu_principal(gestor_de_pasajeros: GestorDePasajeros, gestor_de_vuelos: GestorDeVuelos, gestor_de_reservas: GestorDeReservas) -> None:
    while True:
        mostrar_menu_principal()
        opcion = Herramientas.pedir_entero("Opcion : ")
        if opcion == 0:
            break
        elif opcion == 1:
            gestor_de_pasajeros.menu_pasajero()
        elif opcion == 2:
            gestor_de_vuelos.menu_vuelos()
        elif opcion == 3:
            gestor_de_reservas.menu_reservas()
        else:
            print("Opcion invalida")

def main():
    gestor_de_pasajeros = GestorDePasajeros()
    gestor_de_vuelos = GestorDeVuelos()
    gestor_de_reservas = GestorDeReservas(gestor_de_pasajeros, gestor_de_vuelos)

    opciones = [
        ("0- Salir", lambda: print("Saliendo...")),
        ("1- Gestor de Pasajeros", gestor_de_pasajeros.menu_pasajero),
        ("2- Gestor de Vuelos", gestor_de_vuelos.menu_vuelos),
        ("3- Gestor de Reservas", gestor_de_reservas.menu_reservas)
    ]
    mi_menu = Menu(opciones)
    mi_menu.seleccionar_func("=== Menu Principal ===")

main()