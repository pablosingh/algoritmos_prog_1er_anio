from contextlib import nullcontext


class Fecha:
    def __init__(self, fecha_str):
        fecha_nacimiento_split = fecha_str.split("/")
        self.dia = int(fecha_nacimiento_split[0])
        self.mes = int(fecha_nacimiento_split[1])
        self.anio = int(fecha_nacimiento_split[2])

class Alumno:
    def __init__(self, legajo, nombre, dni, fecha_de_nacimiento: Fecha):
        self.legajo = legajo
        self.nombre = nombre
        self.dni = dni
        self.fecha_de_nac = fecha_de_nacimiento
        self.materias = []

    def __str__(self):
        cadena = f"Alumno ({self.legajo}) {self.nombre} - DNI: {self.dni} - Edad {self.calcular_edad()} "
        for materia in self.materias:
            cadena += materia.__str__()
        return cadena

    def calcular_edad(self):
        dia_actual = 27
        mes_actual = 9
        anio_actual = 2025

        edad = None
        if mes_actual > self.fecha_de_nac.mes:
            edad = anio_actual - self.fecha_de_nac.anio
        elif mes_actual < self.fecha_de_nac.mes:
            edad = anio_actual - self.fecha_de_nac.anio - 1
        elif mes_actual == self.fecha_de_nac.mes:
            if dia_actual < self.fecha_de_nac.dia:
                edad = anio_actual - self.fecha_de_nac.anio - 1
            else:
                edad = anio_actual - self.fecha_de_nac.anio
        return edad

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Materia: ({self.nombre}) "


lista_de_alumnos: list[Alumno] = []

def listar_alumnos():
    for alumno in lista_de_alumnos:
        print(alumno)

def agregar_materia():
    print("Agregando materia")
    alumno_encontrado = buscar_alumno_por_dni()
    nombre_materia = input("Ingrese el nombre del materia: ")
    materia = Materia(nombre_materia)
    alumno_encontrado.materias.append(materia)

def registrar_alumno():
    legajo = len(lista_de_alumnos) + 1
    nombre = input("Ingrese el nombre del alumno: ")
    dni = input(f"Ingrese el DNI de {nombre}: ")
    fecha_de_nacimiento = Fecha(input("Ingrese la fecha de nacimiento (01/03/2020): "))
    nuevo_alumno = Alumno(legajo,nombre, dni, fecha_de_nacimiento)
    lista_de_alumnos.append(nuevo_alumno)
    print(f"Alumno {nombre} ({legajo}) registrado correctamente.")

def buscar_alumno_por_dni():
    dni_a_buscar = input("Ingrese el DNI del alumno a buscar: ")
    for i in range(len(lista_de_alumnos)):
        if lista_de_alumnos[i].dni == dni_a_buscar:
            print(f"Se encontro al alumno {lista_de_alumnos[i]}")
            return lista_de_alumnos[i]
    return False

def mostar_menu():
    print("---- MENU -----")
    print("0- Listar alumnos")
    print("1- Registrar alumno")
    print("2- Buscar alumno por DNI")
    print("3- Calcular promedio de edad de alumnos")
    print("4- Salir")
    print("5- Agregar Materia")

def pedir_opcion_valida():
    opcion = ""
    while opcion not in ("1", "2", "0","3", "4", "5"):
        opcion = input("Ingrese la opcion seleccionada: ")
        if opcion not in ("1", "2", "0","3", "4", "5"):
            print("opción invalida!")
    return opcion

def mostrar_promedio_edades():
    sumatoria = 0
    for i in range(len(lista_de_alumnos)):
        edad = lista_de_alumnos[i].calcular_edad()
        sumatoria += edad
    if len(lista_de_alumnos) > 0:
        print(f"El promedio de edades es: {sumatoria / len(lista_de_alumnos)}")
    else:
        print("Aún no se han cargado alumnos")

def main():
    while True:
        mostar_menu()
        opcion_elegida = pedir_opcion_valida()
        if opcion_elegida == "1":
            registrar_alumno()
        elif opcion_elegida == "2":
            buscar_alumno_por_dni()
        elif opcion_elegida == "3":
            mostrar_promedio_edades()
        elif opcion_elegida == "4":
            break
        elif opcion_elegida == "0":
            listar_alumnos()
        elif opcion_elegida == "5":
            agregar_materia()
        else:
            print("Opcion invalida")

main()