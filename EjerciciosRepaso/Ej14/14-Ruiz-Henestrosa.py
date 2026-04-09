
# Ejercicio 14: Juego de adivinanza
# Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random).
# Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que acierte.
import random

class Adivinanza:
    def __init__(self,numero):
        self.numero=numero
    
    def acertar(self):
        while True:
            try:
                opcion=int(input('Indica un número: '))
                if opcion == self.numero:
                    print(f'Acertaste el número secreto.\nUsaste {contador} intentos.')
                    break
                elif opcion > self.numero:
                    print('más bajo')
                elif opcion < self.numero:
                    print('más alto')
            except:
                print('Algún parámetro es incorreto')
        
juego_1=Adivinanza(random.randint(1,100))

if __name__ == "__main__":
    juego_1.acertar()