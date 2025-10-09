from Cuenta import Cuenta

cuentas: list[Cuenta] = []
numero_id = 0

def muestra_menu():
    print("\n===============================")
    print("0 - Salir")
    print("1 - Agregar Cuenta Bancaria")
    print("2 - Listar Cuentas Bancarias")
    print("3 - Buscar Cuenta por Numero")
    print("4 - Borrar Cuenta Bancaria")
    print("5 - Editar Cuenta Bancaria")

def ingresa_opcion():
    while True:
        opcion = input("Ingrese una opcion : ")
        if opcion.isdigit():
            opcion = int(opcion)
            return opcion
        else:
            print("Opcion no valida")

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresá solo números decimales.-")

def agregar_cuenta_bancaria():
    nombre = input("Ingrese el nombre del cuenta: ")
    apellido = input("Ingrese el apellido: ")
    tipo = input("Ingrese el tipo: ")
    saldo = pedir_float("Ingrese el saldo: ")
    global numero_id
    numero_id +=1
    cuenta = Cuenta(numero_id, nombre, apellido, tipo, saldo)
    cuentas.append(cuenta)

def listar_cuentas_bancarias():
    for cuenta in cuentas:
        print(cuenta)

def buscar_cuenta_por_numero():
    while True:
        numero = input("Ingrese el numero de la cuenta : ")
        if numero.isdigit():
            numero = int(numero)
            break
        else:
            print("Error, No es un nro")
    for i in range(len(cuentas)):
        if cuentas[i].numero == numero:
            print(cuentas[i])
            return cuentas[i], i
    print("No se Encontro la cuenta")
    return None, -1

def borrar_cuenta_bancaria():
    print("Eliminando")
    indice_cuenta_a_buscar = buscar_cuenta_por_numero()[1]
    if indice_cuenta_a_buscar != -1:
        cuentas.pop(indice_cuenta_a_buscar)
        print("Eliminado")

def mostrar_menu_edicion(nombre, apellido, tipo, saldo):
    print("\n===============================")
    print(f"Editando... | {nombre} \t | {apellido} \t | {tipo} \t | {saldo}")
    print("0 - Fin de Edicion")
    print("1 - Editar Nombre")
    print("2 - Editar Apellido")
    print("3 - Editar Tipo")
    print("4 - Editar Saldo")

def editar_cuenta():
    cuenta, indice = buscar_cuenta_por_numero()
    if indice == -1:
        print("Volviendo al menu principal")
        return
    else:
        nombre = cuenta.nombre
        apellido = cuenta.apellido
        tipo = cuenta.tipo
        saldo = cuenta.saldo
    while cuenta:
        mostrar_menu_edicion(nombre, apellido, tipo, saldo)
        opcion = ingresa_opcion()
        if opcion == 0:
            cuentas[indice].nombre = nombre
            cuentas[indice].apellido = apellido
            cuentas[indice].tipo = tipo
            cuentas[indice].saldo = saldo
            print("Guardando")
            break
        elif opcion == 1:
            nombre = input("Ingrese el NUEVO nombre : ")
        elif opcion == 2:
            apellido = input("Ingrese el NUEVO apellido : ")
        elif opcion == 3:
            tipo = input("Ingrese el NUEVO tipo : ")
        elif opcion == 4:
            saldo = pedir_float("Ingrese el NUEVO saldo : ")

def main():
    while True:
        muestra_menu()
        opcion = ingresa_opcion()
        if opcion == 0:
            break
        elif opcion == 1:
            agregar_cuenta_bancaria()
        elif opcion == 2:
            listar_cuentas_bancarias()
        elif opcion == 3:
            buscar_cuenta_por_numero()
        elif opcion == 4:
            borrar_cuenta_bancaria()
        elif opcion == 5:
            editar_cuenta()
        else:
            print("Opcion no valida")

main()

