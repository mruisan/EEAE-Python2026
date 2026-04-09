
# Ejercicio 9: Promedio de notas
# Crea una clase Notas con una lista de calificaciones como atributo.
# Implementa un método que calcule el promedio y otro que devuelva la nota más alta. Añade manejo de
# excepciones para evitar ontas inferiores a 0 o superiores a 10.

class Notas:
    def __init__(self,boletin):
        self.boletin=boletin
    def promedio(self):
        try:
            vali=0
            for i in self.boletin:
                if i >= 0 and i <=10:
                    continue
                else:
                    vali+=1
                    continue
            if vali == 0:
                media= (sum(self.boletin))/(len(self.boletin))
                return round(media,2)
            else:
                return 'Alguna nota es incorreta'
        except:
            return 'Algún parámetro es incorreto'
    def maxi(self):
        orden= sorted(self.boletin)
        return orden[-1]

trimestre_1=Notas([5,7,-6,8,3,4,6,2,9,10,4])
trimestre_2=Notas([5,7,'ocho',8,3,4,6,2,9,10,4])
trimestre_3=Notas([5,7,6,8,3,4,6,2,9,10,4])

if __name__ == "__main__":
    print(trimestre_1.promedio())
    print(trimestre_1.maxi())
    print(trimestre_2.promedio())
    print(trimestre_3.promedio())
