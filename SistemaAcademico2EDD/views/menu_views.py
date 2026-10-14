class MenuVista:
    def mostrar_menu(self):
        print("\n--- SISTEMA ACADÉMICO (MVC) ---")
        print("1. Registrar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Salir")
        return input("Seleccione una opción: ")

    def solicitar_datos_estudiante(self):
        cedula = input("Ingrese cédula: ")
        nombre = input("Ingrese nombre: ")
        apellido = input("Ingrese apellido: ")
        codigo = input("Ingrese código de estudiante: ")
        carrera = input("Ingrese carrera: ")
        return cedula, nombre, apellido, codigo, carrera

    def mostrar_mensaje(self, mensaje):
        print(f"\n[MENSAJE]: {mensaje}")

    def mostrar_lista(self, estudiantes):
        print("\n--- LISTA DE ESTUDIANTES ---")
        if not estudiantes:
            print("No hay estudiantes registrados.")
        for est in estudiantes:
            print(est.obtener_datos())