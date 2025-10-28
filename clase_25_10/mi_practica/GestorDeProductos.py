import pickle
from Product import Product

class GestorDeProductos:

    def __init__(self):
        self.productos: list[Product] = []

    def cargar_productos(self):
        try:
            with open("productos.bin", "rb") as mi_base_de_productos:
                self.productos = pickle.load(mi_base_de_productos)
        except FileNotFoundError:
            self.guardar_productos()

    def guardar_productos(self):
        try:
            with open("productos.bin", "wb") as mi_base_de_productos:
                pickle.dump(self.productos, mi_base_de_productos)
        except:
            print("No se ha podido guardar el archivo")

    def listar_productos(self):
        print(f"---- Listando {len(self.productos)} productos ----")
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, codigo: int) -> Product | None:
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def buscar_producto_por_codigo(self):
        codigo = int(input("Ingrese el codigo del producto que busca: "))
        producto = self.buscar_producto(codigo)
        if producto:
            print(f"Producto encontrado: {producto}")
        else:
            print(f"No se encontró un producto con código '{codigo}'")

    def agregar_nuevo_producto(self):
        producto = Product(-1, "Ficticio", 0)
        codigo = None
        while producto:
            codigo = int(input("Ingrese el código del nuevo producto: "))
            producto = self.buscar_producto(codigo)
            if producto:
                print("El código ingresado ya está en uso, por favor ingrese otro")
        nombre = input(f"Ingrese el nombre del producto {codigo}: ")
        precio = float(input(f"Ingrese el precio del producto {codigo} ({nombre}): "))
        nuevo_producto = Product(codigo, nombre, precio)
        self.productos.append(nuevo_producto)
        self.guardar_productos()

    def modificar_producto_existente(self):
        codigo = int(input("Ingrese el codigo del producto que quiere modificar: "))
        producto = self.buscar_producto(codigo)
        if producto:
            nuevo_nombre = input(
                f"ingrese el nuevo nombre del producto o presione Enter para dejar el mismo ({producto.nombre}): ")
            nuevo_precio = input(
                f"ingrese el nuevo precio del producto o presione Enter para dejar el mismo (${producto.precio}): ")
            hubo_cambios = False
            if nuevo_nombre:
                producto.nombre = nuevo_nombre
                hubo_cambios = True
            if nuevo_precio:
                producto.precio = float(nuevo_precio)
                hubo_cambios = True
            if hubo_cambios:
                self.guardar_productos()
                print("Cambios guardados con exito")
            else:
                print("No se registraron cambios para guardar")
        else:
            print(f"No se encontró un producto con código '{codigo}'")

    def eliminar_producto_existente(self):
        codigo = int(input("Ingrese el codigo del producto que quiere eliminar: "))
        producto = self.buscar_producto(codigo)
        if producto:
            confirmar = input(f"¿Seguro que desea eliminar el producto {producto}? (si/no): ")
            if confirmar.lower() in ("sí", "si"):
                self.productos.remove(producto)
                self.guardar_productos()
                print("Producto eliminado con exito")
            else:
                print("Se ha cancelado la operacion, producto NO eliminado")
        else:
            print(f"No se encontró un producto con código '{codigo}'")

    def mostrar_menu_productos(self)-> None:
        print("============ MENU DE PRODUCTOS ================")
        print("\t0- Volver - Salir")
        print("\t1- Agregar Producto")
        print("\t2- Editar Producto")
        print("\t3- Borrar Producto")
        print("\t4- Listar todos los Productos")

    def menu_productos(self)-> None:
        opciones = ["0", "1", "2", "3", "4"]
        while True:
            self.mostrar_menu_productos()
            opcion = input("\tOpcion : ")
            if opcion in opciones:
                if opcion == "0":
                    break
                elif opcion == "1":
                    self.agregar_nuevo_producto()
                elif opcion == "2":
                    self.modificar_producto_existente()
                elif opcion == "3":
                    self.eliminar_producto_existente()
                elif opcion == "4":
                    self.listar_productos()
            else:
                print("Opcion invalida")