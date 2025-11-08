from Alumno import Alumno
from Herramientas import Herramientas

class GestorDeAlumnos:
    def __init__(self):
        self.alumnos: Alumno = []

    def agregar_alumno(self)->None:
        nombre = input("Ingrese el Nombre/Apellido del Alumno: ")
        dni = Herramientas.pedir_entero("Ingrese el DNI : ")
        email = input("Ingrese el email: ")
        carrera = input("Ingrese la carrera: ")

        self.alumnos.append(Alumno(dni, nombre, email, carrera))
        #self.guardar_clientes()

    def buscar_alumno_por_dni(self)->Alumno | None:
        dni = Herramientas.pedir_entero("Ingrese el DNI a buscar : ")
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    def buscar_alumno(self)->None:
        alumno = self.buscar_alumno_por_dni()
        if alumno:
            print(alumno)
        else:
            print("No se Encontro el alumno")

    def eliminar_alumno_dni(self)->None:
        print("Para Eliminar un Alumno")
        alumno_a_eliminar =  self.buscar_alumno_por_dni()
        if alumno_a_eliminar:
            self.alumnos.remove(alumno_a_eliminar)
        else:
            print("Error - No se encontro el Alumno")

    def editar_alumno(self)->None:
        print("Para Editar un Alumno")
        alumno_a_editar = self.buscar_alumno_por_dni()
        if alumno_a_editar:
            print("Enter para continuar")
            alumno_a_editar.dni = Herramientas.pedir_entero(f"DNI {alumno_a_editar.dni}| Nuevo DNI: ") or alumno_a_editar.dni
            alumno_a_editar.nombre = input(f"{alumno_a_editar.nombre}| Nuevo Nombre: ") or alumno_a_editar.nombre
            alumno_a_editar.email = input(f"{alumno_a_editar.email}| Nuevo Email: ") or alumno_a_editar.email
            alumno_a_editar.carrera = input(f"{alumno_a_editar.carrera}| Nueva Carrera: ") or alumno_a_editar.carrera
        else:
            print("No se encontro el Alumno.-")

    def mostrar_alumnos(self)->None:
        for alumno in self.alumnos:
            print(alumno)

    def mostrar_menu_alumnos(self)->None:
        print("0 - Salir")
        print("1 - Agregar Alumno")
        print("2 - Buscar Alumno / Mostrar detalles de un Alumno")
        print("3 - Editar Alumno")
        print("4 - Eliminar Alumno")
        print("5 - Mostrar todos los alumnos")

    def menu_alumnos(self)->None:
        while True:
            self.menu_alumnos()
            opcion = Herramientas.pedir_entero("Opcion: ")
            if opcion == 0:
                break
            elif opcion == 1:
                self.agregar_alumno()
            elif opcion == 2:
                self.buscar_alumno()
            elif opcion == 3:
                self.editar_alumno()
            elif opcion == 4:
                self.eliminar_alumno_dni()
            elif opcion == 5:
                self.mostrar_alumnos()
            else:
                print("Opcion Invalida")



