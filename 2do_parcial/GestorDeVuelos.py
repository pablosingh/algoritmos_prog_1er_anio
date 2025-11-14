import pickle
from Herramientas import Herramientas
from Vuelo import Vuelo
from FechaHora import FechaHora

class GestorDeVuelos:
    def __init__(self):
        self.vuelos: list[Vuelo] = []
        self.ciudades: list[str] = [
            "Buenos Aires",
            "Catamarca",
            "Chaco",
            "Chubut",
            "Córdoba",
            "Corrientes",
            "Entre Ríos",
            "Formosa",
            "Jujuy",
            "La Pampa",
            "La Rioja",
            "Mendoza",
            "Misiones",
            "Neuquén",
            "Río Negro",
            "Salta",
            "San Juan",
            "San Luis",
            "Santa Cruz",
            "Santa Fe",
            "Santiago del Estero",
            "Tierra del Fuego",
            "Tucumán"
        ]
        self.cargar_vuelos()

    def guardar_vuelos(self) -> None:
        try:
            with open("vuelos.bin", "wb") as archivo:
                pickle.dump(self.vuelos, archivo)
        except FileNotFoundError:
            print("No se ha podido guardar el archivo")

    def cargar_vuelos(self) -> None:
        try:
            with open("vuelos.bin", "rb") as archivo:
                self.vuelos = pickle.load(archivo)
        except FileNotFoundError:
            self.guardar_vuelos()

    def calcular_id(self) -> int:
        if len(self.vuelos) == 0:
            return 1
        else:
            return self.vuelos[len(self.vuelos) - 1].id + 1

    def pedir_ciudad_valida(self, mensaje: str) -> str:
        while True:
            print(mensaje)
            self.mostrar_menu_ciudades(mensaje)
            indice_de_ciudad = Herramientas().pedir_entero("Ingrese el nro de la Ciudad : ") - 1
            if indice_de_ciudad >= 0 and indice_de_ciudad < len(self.ciudades):
                return self.ciudades[indice_de_ciudad]
            else:
                print("El nro de la ciudad es invalido")

    def agregar_vuelo(self) -> None:
        print("=== Agregar Nuevo Vuelo ===")
        origen = self.pedir_ciudad_valida("Origen: ")
        while True:
            destino = self.pedir_ciudad_valida("Destino: ")
            if origen != destino:
                break
            else:
                print("El destino debe ser distinto que el origen")
        fecha_salida = FechaHora(FechaHora.pedir_fecha_hora_valida("Fecha Salida: "))
        fecha_llegada = FechaHora(FechaHora.pedir_fecha_hora_valida("Fecha Llegada: "))
        vuelo = Vuelo(self.calcular_id(), origen, destino, fecha_salida, fecha_llegada)
        self.vuelos.append(vuelo)
        self.guardar_vuelos()
        print("Vuelo agregado correctamente.\n")

    def buscar_vuelo_por_origen_destino(self) -> list[Vuelo]:
        vuelos_encontrados: list[Vuelo] = []
        origen = self.pedir_ciudad_valida("ORIGEN del vuelo a Buscar: ")
        destino = self.pedir_ciudad_valida("DESTINO del vuelo a Buscar: ")

        for vuelo in self.vuelos:
            if vuelo.origen.lower() == origen.lower() and vuelo.destino.lower() == destino.lower():
                vuelos_encontrados.append(vuelo)
        return vuelos_encontrados

    def buscar_vuelo_por_id(self)-> Vuelo | None:
        id = Herramientas.pedir_entero("Ingrese el Id del Vuelo : ")
        for vuelo in self.vuelos:
            if vuelo.id == id:
                return vuelo
        return None

    def buscar_vuelo(self)->None:
        vuelo = self.buscar_vuelo_por_origen_destino()
        if vuelo:
            print(vuelo)
        else:
            print("No se Encontro el vuelo")

    def eliminar_vuelo(self) -> None:
        print("=== Eliminar Vuelo ===")
        vuelo_a_eliminar = self.buscar_vuelo_por_id()
        if vuelo_a_eliminar:
            self.vuelos.remove(vuelo_a_eliminar)
            self.guardar_vuelos()
            print("Vuelo eliminado correctamente.\n")
        else:
            print("Error - No se encontró el vuelo.\n")

    def editar_vuelo(self) -> None:
        print("=== Editar Vuelo ===")
        vuelo_a_editar = self.buscar_vuelo_por_id()
        if vuelo_a_editar:
            if Herramientas.pedir_confirmacion(f"Editar Origen actual: {vuelo_a_editar.origen} "):
                nuevo_origen = self.pedir_ciudad_valida(f"Nuevo origen: ")
                vuelo_a_editar.origen = nuevo_origen
            if Herramientas.pedir_confirmacion(f"Editar Destino actual: {vuelo_a_editar.destino} "):
                nuevo_destino = self.pedir_ciudad_valida(f"Nuevo destino: ")
                vuelo_a_editar.destino = nuevo_destino
            if Herramientas.pedir_confirmacion(f"Editar Fecha Salida actual: {vuelo_a_editar.fecha_salida} "):
                nueva_fecha_salida = FechaHora(FechaHora.pedir_fecha_hora_valida("Nueva Fecha Salida: "))
                vuelo_a_editar.fecha_salida = nueva_fecha_salida
            if Herramientas.pedir_confirmacion(f"Editar Fecha Llegada actual: {vuelo_a_editar.fecha_llegada} "):
                nueva_fecha_llegada = FechaHora(FechaHora.pedir_fecha_hora_valida("Nueva Fecha Llegada: "))
                vuelo_a_editar.fecha_llegada = nueva_fecha_llegada
            self.guardar_vuelos()
            print("Vuelo actualizado correctamente.\n")
        else:
            print("No se encontró el vuelo a editar.\n")

    def mostrar_vuelos(self, vuelos_filtrados: list[Vuelo] = []) -> None:
        print("=== Lista de Vuelos ===")
        if len(vuelos_filtrados):
            for vuelo in vuelos_filtrados:
                print(vuelo)
        elif not self.vuelos:
            print("No hay vuelos registrados.\n")
        else:
            for vuelo in self.vuelos:
                print(vuelo)

    def filtrar_vuelos_por_fecha(self, vuelos_para_filtrar: list[Vuelo] | None)-> list[Vuelo]:
        vuelos_filtrados:list[Vuelo] = []
        fecha_str: str = FechaHora.pedir_fecha_valida_sin_horas()
        dia, mes, anio = map(int, fecha_str.split('/'))
        if vuelos_para_filtrar:
            for vuelo in vuelos_para_filtrar:
                if vuelo.fecha_salida.dia == dia and vuelo.fecha_salida.mes == mes and vuelo.fecha_salida.anio == anio:
                    vuelos_filtrados.append(vuelo)
        else:
            for vuelo in self.vuelos:
                if vuelo.fecha_salida.dia == dia and vuelo.fecha_salida.mes == mes and vuelo.fecha_salida.anio == anio:
                    vuelos_filtrados.append(vuelo)
        return vuelos_filtrados

    def mostrar_menu_vuelos(self) -> None:
        print("===============================================================================")
        print("==== MENÚ DE VUELOS =====")
        print("\t0 - Salir")
        print("\t1 - Agregar Vuelo")
        print("\t2 - Buscar Vuelo")
        print("\t3 - Editar Vuelo")
        print("\t4 - Eliminar Vuelo")
        print("\t5 - Mostrar todos los Vuelos")

    def mostrar_menu_ciudades(self, mensaje: str | None) -> None:
        print("=============================")
        if mensaje:
            print(mensaje)
        print("Ciudades Disponibles: ")
        ancho = 23
        for i in range(len(self.ciudades)):
            cadena: str = ""
            cadena = f"{i+1}- {self.ciudades[i]}"
            while len(cadena) < ancho:
                cadena += " "
            print(cadena, end="")
            if i !=0 and i % 7 == 0:
                print()
            if i == len(self.ciudades)-1:
                print()

    def menu_vuelos(self) -> None:
        while True:
            self.mostrar_menu_vuelos()
            opcion = Herramientas.pedir_entero("Opción: ")
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_vuelo()
            elif opcion == 2:
                self.mostrar_vuelos()
                self.buscar_vuelo()
            elif opcion == 3:
                self.mostrar_vuelos()
                self.editar_vuelo()
            elif opcion == 4:
                self.mostrar_vuelos()
                self.eliminar_vuelo()
            elif opcion == 5:
                self.mostrar_vuelos()
            else:
                print("Opción inválida")
