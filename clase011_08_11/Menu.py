class Menu:
    def __init__(self, arreglo):
        self.arreglo = arreglo

    @staticmethod
    def mostrar_menu(arreglo)->None:
        for i in range(len(arreglo)):
            print("")

    @staticmethod
    def a():
        print("mostrando a")

    @staticmethod
    def b():
        print("mostrando b")

    @staticmethod
    def probando(a) -> None:
        lista = [
            ("mostrar a", Menu.a),
            ("mostrar b", Menu.b)
        ]

        if a == lista[0][0]:
            lista[0][1]()
        elif a == lista[1][0]:
            lista[1][1]()
        else:
            print("No hay coincidencias")

Menu.probando("mostrar a")