from models.persona import Persona

class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, codigo_estudiante, carrera):
        super().__init__(cedula, nombre, apellido)
        self.codigo_estudiante = codigo_estudiante
        self.carrera = carrera

    def obtener_datos(self):
        datos_base = super().obtener_datos()
        return f"{datos_base}, Código: {self.codigo_estudiante}, Carrera: {self.carrera}"

    def a_diccionario(self):
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "codigo_estudiante": self.codigo_estudiante,
            "carrera": self.carrera
        }