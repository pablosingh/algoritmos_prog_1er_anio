class Fecha:
    def __init__(self, fecha_str: str):
        fecha_nacimiento_split = fecha_str.split("/")
        self.dia = int(fecha_nacimiento_split[0])
        self.mes = int(fecha_nacimiento_split[1])
        self.anio = int(fecha_nacimiento_split[2])

class Alumno:
    def __init__(self, legajo: int, nombre: str, dni: str, fecha_de_nacimiento: Fecha):
        self.legajo = legajo
        self.nombre = nombre
        self.dni = dni
        self.fecha_de_nac = fecha_de_nacimiento

    def __str__(self):
        return f"Alumno ({self.legajo}) {self.nombre} - DNI: {self.dni} - Edad {self.calcular_edad()}"

    def calcular_edad(self):
        dia_actual = 4
        mes_actual = 10
        anio_actual = 2025

        if mes_actual > self.fecha_de_nac.mes or (mes_actual == self.fecha_de_nac.mes and dia_actual >= self.fecha_de_nac.dia):
            edad = anio_actual - self.fecha_de_nac.anio
        else:
            edad = anio_actual - self.fecha_de_nac.anio - 1
        return edad

class Materia:
    def __init__(self, codigo:str, nombre: str, horas_semanales:float):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_semanales = horas_semanales

    def __str__(self):
        return f"Materia ({self.codigo}) {self.nombre} - {self.horas_semanales} hs/semana"

class Comision:
    def __init__(self, materia: Materia, dia_de_la_semana: str, hora_incio: float, docente: str, cupo:int):
        self.materia = materia
        self.alumnos: list[Alumno] = []
        self.dia_semana = dia_de_la_semana
        self.profesor = docente
        self.hora_inicio = hora_incio
        self.hora_fin = hora_incio + materia.horas_semanales
        self.cupo =cupo

    def agregar_alumno(self, alumno: Alumno):
        if len(self.alumnos) < self.cupo:
            self.alumnos.append(alumno)
        else:
            raise ValueError(f"No se puede agregar más alumnos. Cupo {self.cupo} alcanzado!")

    def hay_cupo_disponible(self):
        return len(self.alumnos) < self.cupo


    def __str__(self):
        return f"({self.materia.codigo}) {self.materia.nombre} - Se dicta {self.dia_semana} de {self.hora_inicio} a {self.hora_fin} - Alumnos inscritos: {len(self.alumnos)}"

# Listas globales
lista_de_alumnos: list[Alumno] = []
lista_de_materias: list[Materia] = []
lista_de_comisiones: list[Comision] = []

def registrar_comision():
    #necesito la materia
    codigo_a_buscar = input("Ingrese el codigo de la materia para la cual va a crear la comisión: ")
    materia_encontrada: Materia | None = None
    for materia in lista_de_materias:
        if materia.codigo == codigo_a_buscar:
            materia_encontrada = materia
    #necesito el dia de semana, la hora de inicio, el profe que la dicta y el cupo de alumnos que va a tener,
    # esos datos se los pido al usuario
    dia_de_la_semana = input("Ingrese el dia se la semana que se dicta la materia: ")
    hora_inicio = float(input("Ingrese el horario de inicio de las clases: "))
    profesor = input("Ingrese el nombre del docente que dicta la materia: ")
    cupo = int(input("Ingrese la cantidad de alumnos que tiene como cupo esta comisión: "))
    nueva_comision = Comision(materia_encontrada,dia_de_la_semana,hora_inicio,profesor,cupo)
    lista_de_comisiones.append(nueva_comision)
    print(f"Se ha creado correctamente la comision: {nueva_comision}")

def listar_comisiones():
    if not lista_de_comisiones:
        print("No hay comisiones registradas.")
    else:
        print("Listado de comisiones:")
        for comision in lista_de_comisiones:
            print(comision)

def inscribir_alumnos_a_comision():
    #necesito primero la comision y despues el / los alumnos a inscribir
    #pido el codigo de la materia y busco las comisiones que tiene esa materia, se las muestro al usuario y le pido que elija
    #a cual de esas comisiones va a agregar los alumnos
    codigo_a_buscar = input("Ingrese el código de la materia de la cual quiere ver las comisiones diponibles: ")
    comisiones_encontradas: list[Comision] = []
    for comision in lista_de_comisiones:
        if codigo_a_buscar == comision.materia.codigo:
            comisiones_encontradas.append(comision)
    if comisiones_encontradas:
        print(f"Listando comisiones disponibles para la materia con codigo {codigo_a_buscar}:")
        for i in range(len(comisiones_encontradas)):
            print(f"{i+1}: {comisiones_encontradas[i]}")
        indice_de_comision_seleccionada = int(input("Elija una de las comisiones listadas: "))
        comision_seleccionada: Comision = comisiones_encontradas[indice_de_comision_seleccionada-1]
        #si hay cupo disonible agrego uno o mas alumnos siempre que no supere el cupo
        desea_continuar = "si"
        while comision_seleccionada.hay_cupo_disponible() and desea_continuar.lower() == "si":
            alumno_econtrado = buscar_alumno_por_dni()
            if alumno_econtrado is not None:
                comision_seleccionada.agregar_alumno(alumno_econtrado)
            desea_continuar = input("¿Quiere inscribir más alumnos? (si/no)")
    else:
        print(f"No se han encotrado comisiones para la materia con codigo {codigo_a_buscar}")

# Funciones para alumnos
def listar_alumnos():
    if not lista_de_alumnos:
        print("No hay alumnos registrados.")
    else:
        print("Listado de alumnos:")
        for alumno in lista_de_alumnos:
            print(alumno)

def registrar_alumno():
    legajo = len(lista_de_alumnos) + 1
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input(f"Ingrese el DNI de {nombre}: ")
    fecha_de_nacimiento = Fecha(input("Ingrese la fecha de nacimiento (ej: 01/03/2020): "))
    nuevo_alumno = Alumno(legajo, nombre, dni, fecha_de_nacimiento)
    lista_de_alumnos.append(nuevo_alumno)
    print(f"Alumno {nuevo_alumno.nombre} ({nuevo_alumno.legajo}) registrado correctamente.")

def buscar_alumno_por_dni() -> Alumno | None:
    dni_a_buscar = input("Ingrese el DNI del alumno a buscar: ")
    for alumno in lista_de_alumnos:
        if alumno.dni == dni_a_buscar:
            return alumno
    return None

def mostrar_promedio_edades():
    if not lista_de_alumnos:
        print("Aún no se han cargado alumnos.")
        return

    sumatoria = 0
    for alumno in lista_de_alumnos:
        sumatoria += alumno.calcular_edad()
    promedio = sumatoria / len(lista_de_alumnos)
    print(f"El promedio de edades es: {promedio:.2f}")

# Funciones para materias
def registrar_materia():
    codigo = input("Ingrese el código numérico de la materia: ")
    nombre = input("Ingrese el nombre de la materia: ")
    horas = float(input("Ingrese la cantidad de horas semanales: "))
    nueva_materia = Materia(codigo, nombre, horas)
    lista_de_materias.append(nueva_materia)
    print(f"Materia {nombre} registrada correctamente.")

def listar_materias():
    if not lista_de_materias:
        print("No hay materias registradas.")
    else:
        print("Materias registradas:")
        for materia in lista_de_materias:
            print(materia)

def buscar_materia_por_nombre():
    nombre_buscado = input("Ingrese el nombre de la materia a buscar: ").lower()
    nombres_de_materias_encontradas = []
    for materia in lista_de_materias:
        if materia.nombre == nombre_buscado:
            nombres_de_materias_encontradas.append(materia.nombre)
    if nombres_de_materias_encontradas:
        print("Materias encontradas:")
        for nombre_de_materia in nombres_de_materias_encontradas:
            print(nombre_de_materia)
    else:
        print(f"No se encontró ninguna materia con nombre similar a '{nombre_buscado}'.")

# Menú
def mostar_menu():
    print("\n---- MENU -----")
    print("0 - Listar alumnos")
    print("1 - Registrar alumno")
    print("2 - Buscar alumno por DNI")
    print("3 - Calcular promedio de edad de alumnos")
    print("4 - Registrar materia")
    print("5 - Listar materias")
    print("6 - Buscar materia por nombre")
    print("7 - Registrar comision")
    print("8 - Listar comisiones")
    print("9 - Inscribir alumnos a comisiones")
    print("10 - Salir")

def pedir_opcion_valida():
    opciones_validas = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    opcion = ""
    while opcion not in opciones_validas:
        opcion = input("Ingrese la opción seleccionada: ")
        if opcion not in opciones_validas:
            print("¡Opción inválida!")
    return opcion

# Main
def main():
    while True:
        mostar_menu()
        opcion_elegida = pedir_opcion_valida()
        if opcion_elegida == "0":
            listar_alumnos()
        elif opcion_elegida == "1":
            registrar_alumno()
        elif opcion_elegida == "2":
            alumno_encontrado = buscar_alumno_por_dni()
            if alumno_encontrado is not None:
                print(f"Se encontro el alumno: {alumno_encontrado}")
            else:
                print("Alumno no encontrado")
        elif opcion_elegida == "3":
            mostrar_promedio_edades()
        elif opcion_elegida == "4":
            registrar_materia()
        elif opcion_elegida == "5":
            listar_materias()
        elif opcion_elegida == "6":
            buscar_materia_por_nombre()
        elif opcion_elegida == "7":
            registrar_comision()
        elif opcion_elegida == "8":
            listar_comisiones()
        elif opcion_elegida == "9":
            inscribir_alumnos_a_comision()
        elif opcion_elegida == "10":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

# Ejecutar
main()