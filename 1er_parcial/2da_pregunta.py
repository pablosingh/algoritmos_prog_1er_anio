class Curso:
    def __init__(self, codigo: int, nombre: str, descripcion: str, horas: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.horas = horas
        self.categoria = categoria

    def __str__(self):
        return f"Curso {self.codigo} \t| {self.nombre} \t| {self.descripcion} \t| {self.horas} \t| {self.categoria}"


cursos: list[Curso] = []
id_curso = 0

def cargar_curso():
    while True:
        codigo = pedir_entero("Ingrese el codigo del curso: ")
        if not es_codigo_duplicado(codigo):
            break
        else:
            print("Codigo duplicado")

    nombre = input("Ingrese el nombre del curso: ")
    descripcion = input("Ingrese la descripcion: ")
    horas = pedir_float("Ingrese las horas: ")
    categoria = input("Ingrese la Categoria: ")

    cursos.append(Curso(codigo, nombre, descripcion, horas, categoria))

def cargar_hasta_10():
    print("Cargar hasta 10 cursos")
    cantidad = 1
    while cantidad<=10:
        cargar_curso()
        cantidad +=1
        while True:
            si = input("Quiere seguir cargando Si/No : ")
            if si[0] == "n" or si[0] == "N":
                cantidad = 11
                break
            elif si[0] == "s" or si[0] == "S":
                break
            elif si[0] != "n" and si[0] != "N" and si[0] != "s" and si[0] != "S":
                print("Opcion Invalida")

def mostrar_cursos():
    for curso in cursos:
        print(curso)

def buscar_curso_por_codigo():
    codigo = pedir_entero(input("Ingrese el codigo del curso a buscar : "))
    bandera = True
    for i in range(len(cursos)):
        if cursos[i].codigo == codigo:
            print(f"La Categoria a la que pertenece es : {cursos[i].categoria}")
            print(cursos[i])
            bandera = False
    if bandera:
        print("No se encontro el curso")

def curso_mayor_duracion():
    mayor = 0.0
    indice = -1
    for i in range(len(cursos)):
        if cursos[i].horas > mayor:
            indice = i
            mayor = cursos[i].horas
    print(f"El curso de Mayor duracion es : ")
    print(f"{cursos[indice]}")

def es_codigo_duplicado(codigo):
    bandera = False
    for i in range(len(cursos)):
        if cursos[i].codigo == codigo:
            bandera = True
    return bandera

def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingresá solo números decimales.-")

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            entrada = int(entrada)
            return entrada
        else:
            print("No es un entero")
def mostrar_menu():
    print("=================================================")
    print("1- Agregar Curso")
    print("2- Mostrar Cursos")
    print("3- Curso de Mayor duracion")
    print("4- Buscar curso por codigo")
    print("5- Salir")

def ingresa_opcion():
    while True:
        opcion = input("Ingrese una opcion : ")
        if opcion.isdigit():
            opcion = int(opcion)
            return opcion
        else:
            print("Opcion no valida")

def menu():
    while True:
        mostrar_menu()
        opcion = ingresa_opcion()
        if opcion == 1:
            cargar_hasta_10()
        elif opcion == 2:
            mostrar_cursos()
        elif opcion == 3:
            curso_mayor_duracion()
        elif opcion == 4:
            buscar_curso_por_codigo()
        elif opcion == 5:
            break
        else:
            print("Opcion no valida")

menu()