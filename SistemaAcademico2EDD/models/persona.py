class Persona:
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido

    def obtener_datos(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre} {self.apellido}"