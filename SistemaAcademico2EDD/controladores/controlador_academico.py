import json
import os
from models.estudiante import Estudiante

class ControladorAcademico:
    def __init__(self, archivo_json="Data/estudiantes.json"):
        self.archivo_json = archivo_json
        # Asegurar que la carpeta Data exista
        os.makedirs(os.path.dirname(self.archivo_json), exist_ok=True)
        self.estudiantes = []
        self.cargar_desde_json()

    def agregar_estudiante(self, cedula, nombre, apellido, codigo, carrera):
        nuevo_estudiante = Estudiante(cedula, nombre, apellido, codigo, carrera)
        self.estudiantes.append(nuevo_estudiante)
        self.guardar_en_json()
        return "Estudiante registrado con éxito."

    def obtener_estudiantes(self):
        return self.estudiantes

    def guardar_en_json(self):
        datos_ls = [est.a_diccionario() for est in self.estudiantes]
        with open(self.archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(datos_ls, archivo, indent=4, ensure_ascii=False)

    def cargar_desde_json(self):
        if os.path.exists(self.archivo_json):
            with open(self.archivo_json, 'r', encoding='utf-8') as archivo:
                try:
                    datos_ls = json.load(archivo)
                    self.estudiantes = []
                    for item in datos_ls:
                        est = Estudiante(
                            item["cedula"],
                            item["nombre"],
                            item["apellido"],
                            item["codigo_estudiante"],
                            item["carrera"]
                        )
                        self.estudiantes.append(est)
                except json.JSONDecodeError:
                    self.estudiantes = []