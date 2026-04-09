
# Ejercicio 13: Rectángulo
# Crea una clase Rectangulo con atributos para ancho y alto.
# Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.

class Rectoangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    
    def area(self):
        calcular= self.ancho*self.alto
        return calcular
    
    def perimetro(self):
        peri=(self.ancho*2)+(self.alto*2)
        return peri

figura_1=Rectoangulo(10,5)
figura_2=Rectoangulo(20,8)

if __name__ == "__main__":
    print(f'El área del rectángulos es de {figura_1.area()} cm.')
    print(f'El perímetro del rectángulos es de {figura_2.perimetro()} cm.')

