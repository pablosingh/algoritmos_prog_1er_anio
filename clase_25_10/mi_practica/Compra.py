from Herramientas import Herramientas
from Product import Product
from Cliente import Cliente
from FechaHora import FechaHora

class Compra:
    def __init__(self, cliente: Cliente, id: int = None):
        self.id = id
        self.productos: list[Product] = []
        self.cliente = cliente
        self.fecha_hora = FechaHora()

    def __str__(self)-> None:
        productos_str = f"ID Compra: {self.id} | Cliente {self.cliente.nombre} | DNI: {self.cliente.dni} | {self.fecha_hora} \n"
        for i in range(len(self.productos)):
            productos_str += self.productos[i].__str__() + "\n"
        return productos_str

    def agregar_producto(self, producto: Product) -> None:
        self.productos.append(producto)
