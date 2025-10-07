#Un banco tiene 50 cuentas. Se pide hacer un programa que realice las siguientes opciones:

#ALTA: Permitir ingresa los siguientes datos de cada cuenta (Numero de cuenta--- entero. Tipo de cuenta --- carácter (C: cuenta corriente, A: caja de ahorro). Saldo de la cuenta --- flotante.
#MODICACION: Permite cambiar el saldo de una cuenta (se busca por número de cuenta).
#CONSULTA muestra los datos de todas las cuentas.
#CONSULTA POR NUMERO DE CUENTA muestra los datos de una cuenta cualquiera (se busca por número de cuenta).
#SALIR DEL PROGRAMA

class Cuenta:
    """Representa una cuenta bancaria con sus datos."""

    def __init__(self, numero_cuenta: int, tipo_cuenta: str, saldo: float):
        """Inicializa una cuenta bancaria."""
        if tipo_cuenta.upper() not in ('C', 'A'):
            raise ValueError("Tipo de cuenta inválido. Debe ser 'C' (Corriente) o 'A' (Ahorro).")
        if not isinstance(numero_cuenta, int) or numero_cuenta <= 0:
            raise ValueError("El número de cuenta debe ser un entero positivo.")
        if not isinstance(saldo, (int, float)):
            raise ValueError("El saldo debe ser un valor numérico.")

        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta.upper()  # Almacenar en mayúscula para consistencia
        self.saldo = float(saldo)  # Asegurar que sea flotante

    def __str__(self) -> str:
        """Devuelve una representación legible de la cuenta."""
        tipo_str = None
        if self.tipo_cuenta == 'C':
            tipo_str = "Cuenta corriente"
        else:
            tipo_str = "Caja de ahorro"
        # Formatear saldo con 2 decimales y separador de miles si es necesario
        return (f"CUENTA N°: {self.numero_cuenta} - Tipo: {tipo_str} ({self.tipo_cuenta}) "
                f"- Saldo: ${self.saldo:,.2f}")  # Formato de moneda


class Menu:
    """Gestiona la presentación y selección de opciones de un menú bancario."""

    def __init__(self, opciones: [str]):
        if not isinstance(opciones, list):
            raise ValueError("El parametro opciones debe ser una lista de opciones")
        self.opciones_menu = opciones

    def mostrar_menu(self) -> None:
        """Muestra las opciones del menú en la consola."""
        print("\n--- MENÚ BANCARIO ---")
        for opcion in self.opciones_menu:
            print(opcion)
        print("---------------------")

    def pedir_opcion_de_menu_valida(self) -> int:
        """Solicita al usuario una opción del menú y la valida."""
        opcion_seleccionada = ''
        num_opciones = len(self.opciones_menu)
        while not opcion_seleccionada.isdigit() or \
                int(opcion_seleccionada) not in range(1, num_opciones + 1):
            opcion_seleccionada = input(f'Seleccione una opción (1-{num_opciones}): ')
            if not opcion_seleccionada.isdigit() or \
                    int(opcion_seleccionada) not in range(1, num_opciones + 1):
                print(f'Opción no válida. Debe ser un número entre 1 y {num_opciones}.')
        return int(opcion_seleccionada)


class GestorDeCuentas:
    """Gestiona la colección de cuentas bancarias (altas, modificaciones, consultas)."""
    MAX_CUENTAS = 50

    def __init__(self):
        """Inicializa el gestor con una lista vacía de cuentas."""
        self.cuentas: list[Cuenta] = []

    def buscar_cuenta_por_numero(self, numero_cuenta: int) -> Cuenta:
        """Busca una cuenta por su número. Devuelve la Cuenta o None si no se encuentra."""
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                return cuenta
        return None

    def pedir_numero_cuenta_valido(self, mensaje_prompt: str) -> int:
        """
        Solicita un número de cuenta (entero positivo).
        Devuelve el número como entero.
        """
        while True:
            num_str = input(mensaje_prompt).strip().lower()
            try:
                num_int = int(num_str)
                if num_int > 0:
                    return num_int
                else:
                    print("El número de cuenta debe ser un entero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número entero positivo o 'c' para cancelar.")

    def _pedir_tipo_cuenta_valido(self) -> str:
        """Solicita un tipo de cuenta ('C' o 'A')."""
        while True:
            tipo_str = input(
                "Ingrese el tipo de cuenta (C: Corriente, A: Ahorro): ").strip().lower()
            if tipo_str.upper() in ('C', 'A'):
                return tipo_str.upper()
            else:
                print("Tipo de cuenta inválido. Ingrese 'C' o 'A'.")

    def _pedir_saldo_valido(self) -> float:
        """Solicita un saldo inicial (flotante)."""
        while True:
            saldo_str = input("Ingrese el saldo inicial: ").strip().lower()
            try:
                # Reemplazar coma por punto si se usa como decimal
                saldo_float = float(saldo_str.replace(',', '.'))
                return saldo_float
            except ValueError:
                print("Entrada inválida. Por favor ingrese un valor numérico para el saldo (ej: 1500.50).")

    def agregar_cuenta(self):
        """Solicita datos y agrega una nueva cuenta si hay capacidad y el número es único."""
        print("\n--- Alta de Nueva Cuenta ---")

        if len(self.cuentas) >= self.MAX_CUENTAS:
            print(f"Error: Se ha alcanzado la capacidad máxima de {self.MAX_CUENTAS} cuentas.")
            print("No se puede agregar una nueva cuenta.")
            return

        # Pedir número de cuenta asegurando que sea único
        numero_cuenta = None
        while numero_cuenta is None:
            num_temp = self.pedir_numero_cuenta_valido("Ingrese el número para la nueva cuenta (entero positivo): ")
            if self.buscar_cuenta_por_numero(num_temp):
                print(f"Error: El número de cuenta {num_temp} ya existe. Intente con otro.")
            else:
                numero_cuenta = num_temp  # Número válido y único

        # Pedir tipo de cuenta
        tipo_cuenta = self._pedir_tipo_cuenta_valido()

        # Pedir saldo inicial
        saldo = self._pedir_saldo_valido()

        # Crear y agregar la cuenta
        try:
            nueva_cuenta = Cuenta(numero_cuenta, tipo_cuenta, saldo)
            self.cuentas.append(nueva_cuenta)
            print("-" * 28)
            print(f"¡Cuenta N° {numero_cuenta} agregada con éxito!")
            print(nueva_cuenta)
            print("-" * 28)
        except ValueError as e:
            # Esto no debería ocurrir por las validaciones previas, pero es una salvaguarda
            print(f"Error inesperado al crear la cuenta: {e}")
            print("Alta cancelada.")

    def modificar_saldo_cuenta(self):
        """Solicita número de cuenta, la busca y permite modificar su saldo."""
        print("\n--- Modificar Saldo de Cuenta ---")
        if not self.cuentas:
            print("No hay cuentas registradas para modificar.")
            return

        numero_cuenta = self.pedir_numero_cuenta_valido(
            'Ingrese el número de cuenta a modificar: ')

        cuenta_a_modificar = self.buscar_cuenta_por_numero(numero_cuenta)

        if cuenta_a_modificar:
            print(f"Se modificará el saldo de la cuenta: {cuenta_a_modificar}")
            nuevo_saldo = self._pedir_saldo_valido()
            cuenta_a_modificar.saldo = nuevo_saldo  # Actualizar el saldo
            print("-" * 28)
            print(f"¡Saldo de la cuenta {cuenta_a_modificar.numero_cuenta} modificado correctamente!")
            print(f"Nuevo estado: {cuenta_a_modificar}")
            print("-" * 28)
        else:
            print(f'Error: No se encontró ninguna cuenta con el número {numero_cuenta}.')

    def ver_cuentas(self):
        """Muestra un listado de todas las cuentas registradas, ordenadas por número."""
        print("\n--- Listado de Todas las Cuentas ---")
        if not self.cuentas:
            print("No hay cuentas registradas.")
        else:
            for cuenta in self.cuentas:
                print(cuenta)
        print("-" * 35)

    def buscar_y_mostrar_cuenta(self):
        """Pide un número de cuenta, la busca y muestra su información si la encuentra."""
        print("\n--- Buscar Cuenta por Número ---")
        if not self.cuentas:
            print("No hay cuentas registradas para buscar.")
            return

        numero_cuenta = self.pedir_numero_cuenta_valido(
            'Ingrese el número de la cuenta a buscar: ')
        cuenta_buscada = self.buscar_cuenta_por_numero(numero_cuenta)
        if cuenta_buscada:
            print("\n--- Cuenta Encontrada ---")
            print(cuenta_buscada)
            print("------------------------\n")
        else:
            print(f'No se encontró ninguna cuenta con el número {numero_cuenta}.')


class Aplicacion:

    def __init__(self):
        self.gestor_de_cuentas = GestorDeCuentas()

    def ejecutar(self):
        while True:
            menu_cuentas = Menu(
                ['1. Alta de Cuenta', '2. Modificación de Saldo', '3. Consulta de Todas las Cuentas',
                 '4. Consulta por Número de Cuenta', '5. Salir'])
            menu_cuentas.mostrar_menu()
            opcion_menu_cuentas_seleccionada = menu_cuentas.pedir_opcion_de_menu_valida()
            if opcion_menu_cuentas_seleccionada == 1:
                self.gestor_de_cuentas.agregar_cuenta()
            elif opcion_menu_cuentas_seleccionada == 2:
                self.gestor_de_cuentas.modificar_saldo_cuenta()
            elif opcion_menu_cuentas_seleccionada == 3:
                self.gestor_de_cuentas.ver_cuentas()
            elif opcion_menu_cuentas_seleccionada == 4:
                self.gestor_de_cuentas.buscar_y_mostrar_cuenta()
            elif opcion_menu_cuentas_seleccionada == 5:
                print("Gracias por utilizar el programa!")
                break

app = Aplicacion()
app.ejecutar()