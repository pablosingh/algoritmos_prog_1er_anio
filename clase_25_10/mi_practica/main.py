from GestorDeProductos import GestorDeProductos
from GestorDeClientes import GestorDeClientes


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
    print("2- Gestor de Clientes")
    print("3- Gestor Compras")

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
    gestor_de_clientes = GestorDeClientes()
    gestor_de_clientes.cargar_clientes()
    while True:
        mostrar_menu_principal()
        opcion = pedir_opcion_valida()
        if opcion == "0":
            print("Gracias por utilizar el programa")
            break
        elif opcion == "1":
            gestor_de_productos.menu_productos()
        elif opcion == "2":
            gestor_de_clientes.menu_clientes()

main()