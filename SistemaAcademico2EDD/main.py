from controladores.controlador_academico import ControladorAcademico
from views.menu_views import MenuVista

def main():
    controlador = ControladorAcademico()
    vista = MenuVista()

    while True:
        opcion = vista.mostrar_menu()

        if opcion == "1":
            cedula, nombre, apellido, codigo, carrera = vista.solicitar_datos_estudiante()
            resultado = controlador.agregar_estudiante(cedula, nombre, apellido, codigo, carrera)
            vista.mostrar_mensaje(resultado)

        elif opcion == "2":
            estudiantes = controlador.obtener_estudiantes()
            vista.mostrar_lista(estudiantes)

        elif opcion == "3":
            vista.mostrar_mensaje("Saliendo del sistema.Hasta luego!")
            break
        else:
            vista.mostrar_mensaje("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()