class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} se ha creado con éxito.")

    def calificacion(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")

# Creando algunos alumnos
alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("Ana", 3)
alumno3 = Alumno("Pedro", 5)
alumno4 = Alumno("Carmen", 7)
alumno5 = Alumno("Fernando", 4)

# Ejecutando el método calificación para cada alumno
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()
alumno4.calificacion()
alumno5.calificacion()
