
    
# Ejercicio 5: Gestión de estudiantes.
# Crea una clase Estudiante con atributos para nombre, edad y calificación.
# Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación
# mayor o igual a 6).

class Estudiante:
    def __init__(self, nombre,edad):
        self.nombre= nombre
        self.edad= edad
        self.__calificacion= 0

    def setCalificacion(self,calificacion):
        if calificacion >= 0 and calificacion <= 10:
            self.__calificacion=calificacion
        else:
            print("La calificación debe estar entre 0 y 10")

    def getCalificacion(self):
        return self.__calificacion
    
    def comprobar(self):
        if self.getCalificacion() >= 6:
            print("Aprobado")
        else:
            print("Suspendido")

alumno_1=Estudiante("Manuel",45)
alumno_2=Estudiante("Jose",25)

if __name__ == "__main__":
    print(alumno_1.nombre)
    print(alumno_1.edad)
    print(alumno_1.getCalificacion())
    alumno_1.setCalificacion(7)
    print(alumno_1.getCalificacion())
    alumno_1.comprobar()
    print(alumno_2.nombre)
    print(alumno_2.edad)
    print(alumno_2.getCalificacion())
    alumno_2.setCalificacion(12)
    print(alumno_2.getCalificacion())
    alumno_2.comprobar()

