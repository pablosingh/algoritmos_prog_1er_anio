from errno import EILSEQ

from Herramientas import Herramientas
from Compra import Compra
from GestorDeClientes import GestorDeClientes
from GestorDeProductos import GestorDeProductos

class GestorDeCompras:
    def __init__(self, gestor_clientes: GestorDeClientes, gestor_productos: GestorDeProductos):
        self.compras: list[Compra] = []
        self.gestor_clientes: GestorDeClientes = gestor_clientes
        self.gestor_productos: GestorDeProductos = gestor_productos

    def agregar_compra(self)->None:
        print("Nueva Compra: Ingrese su Cliente -")
        while True:
            cliente = self.gestor_clientes.buscar_cliente_por_dni()
            if cliente:
                nueva_compra = Compra(cliente)
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
            si = input("Si / No").strip().lower()
            if si[0] == "n":
                break

    def mostrar_menu_compras(self)-> None:
        print("============ MENU DE COMPRAS ================")
        print("\t0- Volver - Salir")
        print("\t1- Agregar Producto")
        print("\t2- Editar Producto")
        print("\t3- Borrar Producto")
        print("\t4- Listar todos los Productos")




