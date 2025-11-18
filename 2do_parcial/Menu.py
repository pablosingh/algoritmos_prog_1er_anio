from Herramientas import Herramientas

class Menu:
    def __init__(self, opciones = []):
        self.opciones = opciones

    def mostrar_menu(self)->None:
        for i in range(len(self.opciones)):
            print(self.opciones[i][0])

    def seleccionar_func(self, mensaje):
        while True:
            print(mensaje)
            self.mostrar_menu()
            opcion = Herramientas.pedir_entero("Opcion : ")
            if opcion == 0:
                return
            if opcion > 0 and opcion < len(self.opciones):
                self.opciones[opcion][1]()
            else:
                print("Opcion invalida")


