from pickle import dumps, load

class Curso:
    def __init__(self, cod, nombre, desc, prof, nivel, horas, categoria):
        self.codigo = int(cod)
        self.nombre = nombre
        self.descripcion = desc
        self.profesor = prof
        self.nivel = nivel
        self.horas_duracion = float(horas)
        self.categoria = categoria

    def __repr__(self):
        return (f"══════════════════════════════════════════\n"
                f"         Curso: {self.nombre} ({self.codigo})\n"
                f"══════════════════════════════════════════\n"
                f"  Descripción:  {self.descripcion}\n"
                f"  Profesor:     {self.profesor}\n"
                f"  Nivel:        {self.nivel}\n"
                f"  Duración:     {self.horas_duracion} horas\n"
                f"  Categoría:    {self.categoria}\n"
                f"══════════════════════════════════════════\n")

    def obtener_resumen(self) -> str:
        return f"Código: {self.codigo} - Curso: {self.nombre}"



class GestorDeCursos:
    def __init__(self):
        self.limite_de_cursos = 10
        self.cursos: list[Curso] = []

    def __str__(self):
        if len(self.cursos) > 0:
            return str(self.cursos)
        else:
            return "No hay cursos cargados actualmente"

    def agregar_curso(self, nuevo_curso: Curso):
        if len(self.cursos) < self.limite_de_cursos:
            self.cursos.append(nuevo_curso)
        else:
            print("La lista de cursos ya se encuentra llena")

    def eliminar_curso(self, curso_a_eliminar: Curso):
        self.cursos.remove(curso_a_eliminar)

    def mostrar_todos(self):
        if self.cursos:
            print("Listando cursos disponibles")
            for curso in self.cursos:
                print(curso)
        else:
            print("No hay cursos cargados hasta el momento")

    def mostrar_simplificado(self):
        for curso in self.cursos:
            print(curso.obtener_resumen())

    def buscar_por_codigo(self, codigo_a_buscar:int)->Curso:
        for curso in self.cursos:
            if curso.codigo == codigo_a_buscar:
                return curso
        return None

    def obtener_nuevo_codigo(self):
        return len(self.cursos) + 1



gestor_de_cursos = GestorDeCursos()


def escribir_en_binario():
    global gestor_de_cursos
    with open('cursos.bin','wb') as bin_file:
        bin_file.write(dumps(gestor_de_cursos.cursos))

def cargar_desde_binario():
    global gestor_de_cursos
    try:
        with open('cursos.bin', 'rb') as bin_file:
            gestor_de_cursos.cursos = load(bin_file)
    except FileNotFoundError:
        gestor_de_cursos.cursos = []


def buscar_curso_por_codigo_y_mostrar_categoria():
    codigo_a_buscar = int(input("ingrese el código a buscar: "))
    curso_encontrado = None
    for curso in gestor_de_cursos.cursos:
        if curso.codigo == codigo_a_buscar:
            curso_encontrado = curso
    if curso_encontrado:
        print(f"La categoría del curso con código {codigo_a_buscar} es {curso_encontrado.categoria}")
    else:
        print(f"No existe un curso con código {codigo_a_buscar}")

def mostrar_todos_los_cursos():
    global gestor_de_cursos
    gestor_de_cursos.mostrar_todos()

def mostrar_curso_por_codigo():
    global gestor_de_cursos
    codigo_a_buscar = int(input("Ingrese el código del curso que desea ver: "))
    resultado=gestor_de_cursos.buscar_por_codigo(codigo_a_buscar)
    if resultado:
        print(resultado)
    else:
        print(f"No se econtro el curso con código {codigo_a_buscar}")


def crear_nuevo_curso():
    global gestor_de_cursos
    nuevo_codigo = gestor_de_cursos.obtener_nuevo_codigo()
    nuevo_nombre = input("Ingrese en nombre del curso: ")
    nueva_desc = input("Ingrese la descripción del curso: ")
    nuevo_prof = input("Ingrese el nombre del profesor del curso: ")
    nuevo_nivel = input("Ingrese el nivel del curso: ")
    nuevas_horas = float(input("Ingrese las horas de duración del curso: "))
    nueva_categoria = input("Ingrese la categoria del curso: ")
    curso = Curso(nuevo_codigo,nuevo_nombre,nueva_desc, nuevo_prof, nuevo_nivel, nuevas_horas, nueva_categoria)
    gestor_de_cursos.agregar_curso(curso)
    escribir_en_binario()

def actualizar_curso_existente():
    global gestor_de_cursos
    print("Cursos disponibles:")
    gestor_de_cursos.mostrar_simplificado()
    curso_elegido=int(input("Elige el código curso que quieres modificar: "))
    curso_encontrado = gestor_de_cursos.buscar_por_codigo(curso_elegido)
    if curso_encontrado:
        nuevo_nombre = input("Ingrese el nuevo nombre del curso (Enter para manter el actual): ")
        nueva_desc = input("Ingrese la nueva descripción del curso (Enter para manter el actual): ")
        nuevo_prof = input("Ingrese el nuevo nombre del profesor del curso (Enter para manter el actual): ")
        nuevo_nivel = input("Ingrese el nuevo nivel del curso (Enter para manter el actual): ")
        nuevas_horas = float(input("Ingrese las nuevas horas de duración del curso (Enter para manter el actual): "))
        nueva_categoria = input("Ingrese la nueva categoria del curso (Enter para manter el actual): ")
        if nuevo_nombre:
            curso_encontrado.nombre=nuevo_nombre
        if nueva_desc:
            curso_encontrado.descripcion=nueva_desc
        if nuevo_prof:
            curso_encontrado.profesor=nuevo_prof
        if nuevo_nivel:
            curso_encontrado.nivel=nuevo_nivel
        if nuevas_horas:
            curso_encontrado.horas_duracion=nuevas_horas
        if nueva_categoria:
            curso_encontrado.categoria=nueva_categoria
        escribir_en_binario()
        print("El curso se ha actualizado correctamente")
        print(curso_encontrado)
    else:
        print(f"No se encontro el curso con código '{curso_elegido}'")

def eliminar_curso_existente():
    global gestor_de_cursos
    print("Cursos disponibles:")
    gestor_de_cursos.mostrar_simplificado()
    curso_elegido = int(input("Elige el código curso que quieres eliminar: "))
    curso_encontrado = gestor_de_cursos.buscar_por_codigo(curso_elegido)
    if curso_encontrado:
        confirmar = input(f"Confirma que desea eliminar el curso:\n{curso_encontrado}\nResponder Si/no: ")
        if confirmar.lower() in ('sí','si','s'):
            gestor_de_cursos.eliminar_curso(curso_encontrado)
            escribir_en_binario()
            print("Se ha eliminado correctamente el curso")
        else:
            print("Eliminación cancelada!")
    else:
        print(f"No se encontro el curso con código '{curso_elegido}'")

OPCIONES_MENU_PRINCIPAL = ["crear curso","mostrar cursos", "mostrar un curso","actualizar curso","eliminar curso","salir"]

def mostrar_opciones_menu_principal():
    print(f"Las opciones disponibles son: {OPCIONES_MENU_PRINCIPAL}")


def menu_principal():
    while True:
        print("---- MENU PRINCIPAL -----")
        mostrar_opciones_menu_principal()
        opcion = input("ingrese la opcion seleccionada: ")
        if opcion == OPCIONES_MENU_PRINCIPAL[0]:
            crear_nuevo_curso()
        elif opcion == OPCIONES_MENU_PRINCIPAL[1]:
            mostrar_todos_los_cursos()
        elif opcion == OPCIONES_MENU_PRINCIPAL[2]:
            mostrar_curso_por_codigo()
        elif opcion == OPCIONES_MENU_PRINCIPAL[3]:
            actualizar_curso_existente()
        elif opcion == OPCIONES_MENU_PRINCIPAL[4]:
            eliminar_curso_existente()
        elif opcion == OPCIONES_MENU_PRINCIPAL[5]:
            print("Muchas gracias por usar el programa.")
            break
        else:
            print("La opción ingresada no es válida")

cargar_desde_binario()
menu_principal()