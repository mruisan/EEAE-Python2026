
# Ejercicio 1: Calculadora básica con clases
# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
# Incluye un constructor que inicialice los dos números como atributos.

class Calculadora:
    def __init__(self, num_1, num_2):
        self.numero_1= num_1
        self.numero_2= num_2

    def sumar(self):
        return f"La suma de {self.numero_1} + {self.numero_2} = {self.numero_1+self.numero_2}"
    def restar (self):
        return f"La resta de {self.numero_1} - {self.numero_2} = {self.numero_1-self.numero_2}"
    def multiplicar (self):
        return f"La multiplicación de {self.numero_1} * {self.numero_2} = {self.numero_1*self.numero_2}"
    def dividir (self):
        return f"La división de {self.numero_1} / {self.numero_2} = {self.numero_1/self.numero_2:.2f}"
    
calculo_1= Calculadora(5,5)
calculo_2= Calculadora(5,3)

if __name__ == "__main__":
    print(calculo_1.sumar())
    print(calculo_2.restar())
    print(calculo_1.multiplicar())
    print(calculo_2.dividir())

