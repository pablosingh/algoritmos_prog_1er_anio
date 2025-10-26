import pickle
import os
from datetime import datetime
import re

# --- MODELOS ---


class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    'Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"


class Cliente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: Fecha):
        if not dni.isdigit() or len(dni) < 7:
            raise ValueError(
                "El DNI debe ser numérico y tener al menos 7 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError(
                "La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Cliente {self.nombre} - DNI: {self.dni} - Nacimiento: {self.fecha_nacimiento}"


class Product:
    def __init__(self, cod: int, name: str, price: float):
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.codigo: int = cod
        self.nombre: str = name
        self.precio: float = price

    def __str__(self):
        return f"Producto ({self.codigo}): {self.nombre} - Precio: ${self.precio:.2f}"

    def aplicar_descuento(self, porcentaje: float) -> float:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        if not (1 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 1 y 100.")
        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)

# --- GESTORES CRUD ---


class GestorDeProductos:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.productos = self._cargar()

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.productos, f)

    def _buscar_por_codigo(self, codigo: int):
        return next((p for p in self.productos if p.codigo == codigo), None)

    def _input_codigo(self, mensaje="Ingrese el código del producto: "):
        try:
            return int(input(mensaje))
        except ValueError:
            print("Código inválido.")
            return None

    def listar_productos(self):
        if not self.productos:
            print("No hay productos para mostrar.")
            return
        for p in self.productos:
            print(p)

    def buscar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def agregar_producto(self):
        codigo = self._input_codigo("Nuevo código: ")
        if codigo is None:
            return
        if self._buscar_por_codigo(codigo):
            print("Ya existe un producto con ese código.")
            return
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                return
            producto = Product(codigo, nombre, precio)
            self.productos.append(producto)
            self._guardar()
            print("Producto agregado.")
        except ValueError:
            print("Precio inválido.")

    def modificar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip()
        if nuevo_nombre:
            producto.nombre = nuevo_nombre
        nuevo_precio = input(f"Nuevo precio ({producto.precio}): ").strip()
        if nuevo_precio:
            try:
                precio = float(nuevo_precio)
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    return
                producto.precio = precio
            except ValueError:
                print("Precio inválido.")
                return
        self._guardar()
        print("Producto modificado.")

    def eliminar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        confirmar = input(
            f"¿Seguro que desea eliminar '{producto.nombre}'? (s/n): ").lower()
        if confirmar == "s":
            self.productos.remove(producto)
            self._guardar()
            print("Producto eliminado.")

    def guardar(self):
        self._guardar()
        print("Cambios guardados.")


class GestorDeClientes:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.clientes = self._cargar()

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.clientes, f)

    def _buscar_por_dni(self, dni: str):
        return next((c for c in self.clientes if c.dni == dni), None)

    def _input_dni(self, mensaje="Ingrese el DNI: "):
        dni = input(mensaje).strip()
        if not dni.isdigit() or len(dni) < 7:
            print("DNI inválido. Debe ser numérico y tener al menos 7 dígitos.")
            return None
        return dni

    def _pedir_fecha_de_nacimiento_valida(self):
        while True:
            fecha_str = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            try:
                return Fecha(fecha_str)
            except ValueError:
                print("Error en el formato. Intente nuevamente.")

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes para mostrar.")
            return
        for c in self.clientes:
            print(c)

    def buscar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if cliente:
            print(cliente)
        else:
            print("Cliente no encontrado.")

    def agregar_cliente(self):
        dni = self._input_dni("Nuevo DNI: ")
        if dni is None:
            return
        if self._buscar_por_dni(dni):
            print("Ya existe un cliente con ese DNI.")
            return
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        fecha_nacimiento = self._pedir_fecha_de_nacimiento_valida()
        cliente = Cliente(dni, nombre, fecha_nacimiento)
        self.clientes.append(cliente)
        self._guardar()
        print("Cliente agregado.")

    def modificar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre ({cliente.nombre}): ").strip()
        cliente.nombre = nuevo_nombre
        cliente.fecha_nacimiento = self._pedir_fecha_de_nacimiento_valida()
        self._guardar()
        print("Cliente modificado.")

    def eliminar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        confirmar = input(
            f"¿Seguro que desea eliminar al cliente '{cliente.nombre}'? (s/n): ").lower()
        if confirmar == "s":
            self.clientes.remove(cliente)
            self._guardar()
            print("Cliente eliminado.")

    def guardar(self):
        self._guardar()
        print("Cambios guardados.")


# --- MENÚ ---

class Menu:
    def __init__(self, opciones: list[str]):
        self.opciones = opciones

    def mostrar(self):
        print("\n--- Menú ---")
        for i, texto in enumerate(self.opciones, 1):
            print(f"{i}. {texto}")

    def pedir_opcion(self) -> int:
        while True:
            try:
                seleccion = int(input("Seleccione una opción: "))
                if 1 <= seleccion <= len(self.opciones):
                    return seleccion
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Debe ingresar un número entero válido.")

# --- MENÚS PRINCIPALES Y SECUNDARIOS ---


def menu_clientes(gestor_clientes: GestorDeClientes):
    menu = Menu([
        "Listar clientes",
        "Buscar cliente por DNI",
        "Agregar cliente",
        "Modificar cliente",
        "Eliminar cliente",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestor_clientes.listar_clientes()
        elif opcion == 2:
            gestor_clientes.buscar_cliente()
        elif opcion == 3:
            gestor_clientes.agregar_cliente()
        elif opcion == 4:
            gestor_clientes.modificar_cliente()
        elif opcion == 5:
            gestor_clientes.eliminar_cliente()
        elif opcion == 6:
            gestor_clientes.guardar()
        elif opcion == 7:
            break


def menu_productos(gestor_productos: GestorDeProductos):
    menu = Menu([
        "Listar productos",
        "Buscar producto por código",
        "Agregar producto",
        "Modificar producto",
        "Eliminar producto",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestor_productos.listar_productos()
        elif opcion == 2:
            gestor_productos.buscar_producto()
        elif opcion == 3:
            gestor_productos.agregar_producto()
        elif opcion == 4:
            gestor_productos.modificar_producto()
        elif opcion == 5:
            gestor_productos.eliminar_producto()
        elif opcion == 6:
            gestor_productos.guardar()
        elif opcion == 7:
            break


def main():
    gestor_productos = GestorDeProductos("productos.bin")
    gestor_clientes = GestorDeClientes("clientes.bin")

    menu_principal = Menu([
        "Gestión de Productos",
        "Gestión de Clientes",
        "Salir"
    ])

    while True:
        menu_principal.mostrar()
        opcion = menu_principal.pedir_opcion()
        if opcion == 1:
            menu_productos(gestor_productos)
        elif opcion == 2:
            menu_clientes(gestor_clientes)
        elif opcion == 3:
            print("Saliendo del programa...")
            break


main()