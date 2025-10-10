from Cuenta import Cuenta

class Gestor_de_cuentas:
    cuentas: list[Cuenta] = []
    numero_id = 0

    def muestra_menu(self):
        print("\n===============================")
        print("0 - Salir")
        print("1 - Agregar Cuenta Bancaria")
        print("2 - Listar Cuentas Bancarias")
        print("3 - Buscar Cuenta por Numero")
        print("4 - Borrar Cuenta Bancaria")
        print("5 - Editar Cuenta Bancaria")

    def ingresa_opcion(self):
        while True:
            opcion = input("Ingrese una opcion : ")
            if opcion.isdigit():
                opcion = int(opcion)
                return opcion
            else:
                print("Opcion no valida")

    def pedir_float(self, mensaje):
        while True:
            try:
                return float(input(mensaje))
            except ValueError:
                print("Ingresá solo números decimales.-")

    def agregar_cuenta_bancaria(self):
        nombre = input("Ingrese el nombre del cuenta: ")
        apellido = input("Ingrese el apellido: ")
        tipo = input("Ingrese el tipo: ")
        saldo = self.pedir_float("Ingrese el saldo: ")
        self.numero_id +=1
        cuenta = Cuenta(self.numero_id, nombre, apellido, tipo, saldo)
        self.cuentas.append(cuenta)

    def listar_cuentas_bancarias(self):
        for cuenta in self.cuentas:
            print(cuenta)

    def buscar_cuenta_por_numero(self):
        while True:
            numero = input("Ingrese el numero de la cuenta : ")
            if numero.isdigit():
                numero = int(numero)
                break
            else:
                print("Error, No es un nro")
        for i in range(len(self.cuentas)):
            if self.cuentas[i].numero == numero:
                print(self.cuentas[i])
                return self.cuentas[i], i
        print("No se Encontro la cuenta")
        return None, -1

    def borrar_cuenta_bancaria(self):
        print("Eliminando")
        indice_cuenta_a_buscar = self.buscar_cuenta_por_numero()[1]
        if indice_cuenta_a_buscar != -1:
            self.cuentas.pop(indice_cuenta_a_buscar)
            print("Eliminado")

    def mostrar_menu_edicion(self, nombre, apellido, tipo, saldo):
        print("\n===============================")
        print(f"Editando... | {nombre} \t | {apellido} \t | {tipo} \t | {saldo}")
        print("0 - Fin de Edicion")
        print("1 - Editar Nombre")
        print("2 - Editar Apellido")
        print("3 - Editar Tipo")
        print("4 - Editar Saldo")

    def editar_cuenta(self):
        cuenta, indice = self.buscar_cuenta_por_numero()
        if indice == -1:
            print("Volviendo al menu principal")
            return
        else:
            nombre = cuenta.nombre
            apellido = cuenta.apellido
            tipo = cuenta.tipo
            saldo = cuenta.saldo
        while cuenta:
            self.mostrar_menu_edicion(nombre, apellido, tipo, saldo)
            opcion = self.ingresa_opcion()
            if opcion == 0:
                self.cuentas[indice].nombre = nombre
                self.cuentas[indice].apellido = apellido
                self.cuentas[indice].tipo = tipo
                self.cuentas[indice].saldo = saldo
                print("Guardando")
                break
            elif opcion == 1:
                nombre = input("Ingrese el NUEVO nombre : ")
            elif opcion == 2:
                apellido = input("Ingrese el NUEVO apellido : ")
            elif opcion == 3:
                tipo = input("Ingrese el NUEVO tipo : ")
            elif opcion == 4:
                saldo = self.pedir_float("Ingrese el NUEVO saldo : ")

    def menu(self):
        while True:
            self.muestra_menu()
            opcion = self.ingresa_opcion()
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_cuenta_bancaria()
            elif opcion == 2:
                self.listar_cuentas_bancarias()
            elif opcion == 3:
                self.buscar_cuenta_por_numero()
            elif opcion == 4:
                self.borrar_cuenta_bancaria()
            elif opcion == 5:
                self.editar_cuenta()
            else:
                print("Opcion no valida")