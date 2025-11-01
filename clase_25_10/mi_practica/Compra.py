from Herramientas import Herramientas
from Product import Product
from Cliente import Cliente

class Compra:
    def __init__(self, cliente: Cliente):
        self.productos: list[Product] = []
        self.cliente = cliente

    def __str__(self)-> None:
        print(f"Compra del Cliente {self.cliente.nombre} | DNI: {self.cliente.dni}")
        productos_str = ""
        for i in range(len(self.productos)):
            productos_str += self.productos[i].nombre + "\n"

    def agregar_producto(self, producto: Product) -> None:
        self.productos.append(producto)
