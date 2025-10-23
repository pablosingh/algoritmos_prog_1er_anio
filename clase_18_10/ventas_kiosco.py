lista_de_ventas: list[str] = []
file_name = 'ventas.txt'

def mostrar_menu():
    print("---- MENU ----")
    print("1 - Registrar venta")
    print("2 - Listar ventas registradas")
    print("3 - Salir")

def pedir_opcion_de_menu_valida():
    opcion_seleccionada = ""
    opciones_validas = ["1", "2", "3"]
    while opcion_seleccionada not in opciones_validas:
        opcion_seleccionada = input("Seleccione una opción: ")
        if opcion_seleccionada not in opciones_validas:
            print("Opción invalida, intente nuevamente!")
    return opcion_seleccionada

def registrar_venta():
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio del {producto}: "))
    cantidad = int(input(f"¿Que cantidad de {producto} lleva el cliente?: "))
    registro_de_producto = f"{producto},{cantidad},{precio}\n"
    lista_de_ventas.append(registro_de_producto)
    with open(file_name, 'a') as ventas_file:
        ventas_file.write(registro_de_producto)
    print("Venta registrada correctmante")

def listar_ventas():
    if lista_de_ventas:
        for venta in lista_de_ventas:
            print(venta, end="")
    else:
        print("Aun no se han regitrado ventas")


def mostrar_menu_y_procesar_opcion():
    while True:
        mostrar_menu()
        opcion = pedir_opcion_de_menu_valida()
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        else:
            print("Gracias. Chau")
            break

def precargar_lista_de_ventas():
    with open(file_name, 'r') as archivo_de_ventas:
        for linea in archivo_de_ventas:
            lista_de_ventas.append(linea)

precargar_lista_de_ventas()
mostrar_menu_y_procesar_opcion()