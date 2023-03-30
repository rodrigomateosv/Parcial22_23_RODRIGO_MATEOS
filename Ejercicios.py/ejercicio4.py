import unittest
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

    def __str__(self):
        return f"Alumno: {self.nombre}, Nota: {self.nota}"

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

class TestEjercicios(unittest.TestCase):
    def test_calificacion(self):
        self.assertEqual(Alumno("Juan", 7).calificacion(), "El alumno Juan ha aprobado")
        self.assertEqual(Alumno("Pedro", 4).calificacion(), "El alumno Pedro ha suspendido")
        self.assertEqual(Alumno("Maria", 6).calificacion(), "El alumno Maria ha aprobado")

    def test__str__(self):
        self.assertEqual(Alumno("Juan", 7).__str__(), "El alumno Juan tiene una nota de 7")
        self.assertEqual(Alumno("Pedro", 4).__str__(), "El alumno Pedro tiene una nota de 4")
        self.assertEqual(Alumno("Maria", 6).__str__(), "El alumno Maria tiene una nota de 6")


if __name__ == '__main__':
    unittest.main()
