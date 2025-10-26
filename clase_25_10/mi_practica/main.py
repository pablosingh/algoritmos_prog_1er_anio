from GestorDeProductos import GestorDeProductos

def mostrar_menu():
    print("--- MENU DE PRODUCTOS ---")
    print("1- Listar productos")
    print("2- Buscar producto por codigo")
    print("3- Agregar nuevo producto")
    print("4- Modificar producto existente")
    print("5- Eliminar producto")
    print("6- Guardar cambios")
    print("7- Salir")

def mostrar_menu_principal()-> None:
    print("--- MENU PRINCIPAL ---")
    print("0- Salir")
    print("1- Gestor de Productos")
    print("2- Gestor de ¨Clientes")

def pedir_opcion_valida()-> str:
    opciones_validas = ["0","1","2"]
    while True:
        opcion = input("Seleccione una ocion: ")
        if opcion not in opciones_validas:
            print("Opcion invalida por favor intente nuevamente!")
        else:
            return opcion

def main():
    gestor_de_productos = GestorDeProductos()
    gestor_de_productos.cargar_productos()
    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion_valida()
        if opcion == "1":
            gestor_de_productos.listar_productos()
        elif opcion == "2":
            gestor_de_productos.buscar_producto_por_codigo()
        elif opcion == "3":
            gestor_de_productos.agregar_nuevo_producto()
        elif opcion == "4":
            gestor_de_productos.modificar_producto_existente()
        elif opcion == "5":
            gestor_de_productos.eliminar_producto_existente()
        elif opcion == "6":
            print("Guardando productos...")
            gestor_de_productos.guardar_productos()
            print("Productos guardados con éxito")
        elif opcion == "7":
            print("Gracias por utilizar el programa")
            break
        else:
            print("Opción inválida")

main()