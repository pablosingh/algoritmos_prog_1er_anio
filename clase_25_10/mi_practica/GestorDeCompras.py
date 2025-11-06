import pickle
from Herramientas import Herramientas
from Compra import Compra
from GestorDeClientes import GestorDeClientes
from GestorDeProductos import GestorDeProductos

class GestorDeCompras:
    def __init__(self, gestor_clientes: GestorDeClientes, gestor_productos: GestorDeProductos):
        self.compras: list[Compra] = []
        self.gestor_clientes: GestorDeClientes = gestor_clientes
        self.gestor_productos: GestorDeProductos = gestor_productos

    def calcular_id(self) -> int:
        if len(self.compras) == 0:
            return 1
        else:
            return self.compras[len(self.compras) - 1].id + 1

    def guardar_compras(self)-> None:
        try:
            with open("compras.bin", "wb") as archivo:
                pickle.dump(self.compras, archivo)
        except FileNotFoundError:
            print("No se ha podido guardar el archivo")

    def cargar_compras(self)-> None:
        try:
            with open("compras.bin", "rb") as archivo:
                self.compras = pickle.load(archivo)
        except FileNotFoundError:
            self.guardar_compras()


    def agregar_compra(self)->None:
        print("Nueva Compra: Ingrese su Cliente -")
        while True:
            cliente = self.gestor_clientes.buscar_cliente_por_dni()
            if cliente:
                nueva_compra = Compra(cliente, self.calcular_id() )
                break
            else:
                print("Intenteló de nuevo.-")

        while True:
            codigo = Herramientas.pedir_entero("Codigo del producto a comprar : ")
            producto = self.gestor_productos.buscar_producto(codigo)
            if producto:
                nueva_compra.agregar_producto(producto)
            else:
                print("Producto No encontrado: Vuelva a intentarlo.-")

            print("Desea seguir agregando productos")
            si = input("Si / No : ").strip().lower()
            if si[0] == "n":
                self.compras.append(nueva_compra)
                self.guardar_compras()
                break

    def buscar_compra_por_id(self) -> Compra | None:
        id = Herramientas.pedir_entero("ID de la compra a buscar : ")
        for compra in self.compras:
            if compra.id == id:
                return compra
        return None

    def borrar_compra(self):
        compra = self.buscar_compra_por_id()
        if compra:
            self.compras.remove(compra)
            self.guardar_compras()
        else:
            print("No existe la compra")

    def mostrar_menu_compras(self)-> None:
        print("============ MENU DE COMPRAS ================")
        print("\t0- Volver - Salir")
        print("\t1- Nueva Compra")
        print("\t2- Borrar Compra")
        print("\t3- Mostrar todas las Compras")

    def mostrar_compras(self)-> None:
        print("Mostrando Compras")
        for compra in self.compras:
            print(compra)

    def menu_compras(self)-> None:
        opciones = ["0", "1", "2", "3", "4"]
        while True:
            self.mostrar_menu_compras()
            opcion = input("\tOpcion : ")
            if opcion in opciones:
                if opcion == "0":
                    break
                elif opcion == "1":
                    self.agregar_compra()
                elif opcion == "2":
                    self.borrar_compra()
                elif opcion == "3":
                    self.mostrar_compras()
            else:
                print("Opcion invalida")


