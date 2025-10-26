import pickle

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

productos: list[Product] = []

def cargar_productos():
    global productos
    with open("productos.bin", "rb") as mi_base_de_productos:
        productos = pickle.load(mi_base_de_productos)

def guardar_productos():
    with open("productos.bin", "wb") as mi_base_de_productos:
        pickle.dump(productos, mi_base_de_productos)

def listar_productos():
    print(f"---- Listando {len(productos)} productos ----")
    for producto in productos:
        print(producto)

def mostrar_menu():
    print("--- MENU PRINCIPAL ---")
    print("1- Listar productos")
    print("2- Buscar producto por codigo")
    print("3- Agregar nuevo producto")
    print("4- Modificar producto existente")
    print("5- Eliminar producto")
    print("6- Guardar cambios")
    print("7- Salir")

def pedir_opcion_valida():
    opciones_validas = ["1","2","3","4","5","6","7"]
    opcion_elegida = ""
    while opcion_elegida not in opciones_validas:
        opcion_elegida = input(f"Seleccione una de las opciones {opciones_validas}: ")
        if opcion_elegida not in opciones_validas:
            print("Opción invalida por favor intente nuevamente!")
    return opcion_elegida

def buscar_producto(codigo: int) -> Product | None:
    for producto in productos:
        if producto.codigo == codigo:
            return producto
    return None

def buscar_producto_por_codigo():
    codigo = int(input("Ingrese el codigo del producto que busca: "))
    producto = buscar_producto(codigo)
    if producto:
        print(f"Producto encontrado: {producto}")
    else:
        print(f"No se encontró un producto con código '{codigo}'")

def agregar_nuevo_producto():
    producto = Product(-1,"Ficticio",0)
    codigo = None
    while producto:
        codigo = int(input("Ingrese el código del nuevo producto: "))
        producto = buscar_producto(codigo)
        if producto:
            print("El código ingresado ya está en uso, por favor ingrese otro")
    nombre = input(f"Ingrese el nombre del producto {codigo}: ")
    precio = float(input(f"Ingrese el precio del producto {codigo} ({nombre}): "))
    nuevo_producto = Product(codigo,nombre, precio)
    productos.append(nuevo_producto)
    guardar_productos()

def modificar_producto_existente():
    codigo = int(input("Ingrese el codigo del producto que quiere modificar: "))
    producto = buscar_producto(codigo)
    if producto:
        nuevo_nombre = input(f"ingrese el nuevo nombre del producto o presione Enter para dejar el mismo ({producto.nombre}): ")
        nuevo_precio = input(f"ingrese el nuevo precio del producto o presione Enter para dejar el mismo (${producto.precio}): ")
        hubo_cambios = False
        if nuevo_nombre:
            producto.nombre = nuevo_nombre
            hubo_cambios = True
        if nuevo_precio:
            producto.precio = float(nuevo_precio)
            hubo_cambios = True
        if hubo_cambios:
            guardar_productos()
            print("Cambios guardados con exito")
        else:
            print("No se registraron cambios para guardar")
    else:
        print(f"No se encontró un producto con código '{codigo}'")

def eliminar_producto_existente():
    codigo = int(input("Ingrese el codigo del producto que quiere eliminar: "))
    producto = buscar_producto(codigo)
    if producto:
        confirmar = input(f"¿Seguro que desea eliminar el producto {producto}? (si/no): ")
        if confirmar.lower() in ("sí", "si"):
            productos.remove(producto)
            guardar_productos()
            print("Producto eliminado con exito")
        else:
            print("Se ha cancelado la operacion, producto NO eliminado")
    else:
        print(f"No se encontró un producto con código '{codigo}'")

def main():
    cargar_productos()
    while True:
        mostrar_menu()
        opcion = pedir_opcion_valida()
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            buscar_producto_por_codigo()
        elif opcion == "3":
            agregar_nuevo_producto()
        elif opcion == "4":
            modificar_producto_existente()
        elif opcion == "5":
            eliminar_producto_existente()
        elif opcion == "6":
            print("Guardando productos...")
            guardar_productos()
            print("Productos guardados con éxito")
        elif opcion == "7":
            print("Gracias por utilizar el programa")
            break
        else:
            print("Opción inválida")

main()