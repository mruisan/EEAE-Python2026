
# Ejercicio 10: Simulador de dado
# Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
# Incluye un método para tirar el dado y otro para mostrar el resultado.
# EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)

from random import randint

class Dado:
    def __init__(self,caras):
        self.caras=caras
        
    def lanzamiento(self):
        return randint(1,self.caras)
    
    def resultado(self):
        cara=self.lanzamiento()
        return cara

d2= Dado(2)
d4= Dado(4)
d6= Dado(6)
d8= Dado(8)
d10= Dado(10)
d12= Dado(12)
d20= Dado(20)

if __name__ == "__main__":
    while True:
        print('MENÚ\n')
        print('Pulsa 1 para seleccionar el dado d2')
        print('Pulsa 2 para seleccionar el dado d4')
        print('Pulsa 3 para seleccionar el dado d6')
        print('Pulsa 4 para seleccionar el dado d8')
        print('Pulsa 5 para seleccionar el dado d10')
        print('Pulsa 6 para seleccionar el dado d12')
        print('Pulsa 7 para seleccionar el dado d20')
        print('Pulsa 0 para salir')
        opcion= int(input('Indique su opción: '))
        if opcion == 1:
            print(f'Al lanzar el dado d2, ha salido {d2.resultado()}.')
        elif opcion == 2:
            print(f'Al lanzar el dado d4, ha salido {d4.resultado()}.')
        elif opcion == 3:
            print(f'Al lanzar el dado d6, ha salido {d6.resultado()}.')
        elif opcion == 4:
            print(f'Al lanzar el dado d8, ha salido {d8.resultado()}.')
        elif opcion == 5:
            print(f'Al lanzar el dado d10, ha salido {d10.resultado()}.')
        elif opcion == 6:
            print(f'Al lanzar el dado d12, ha salido {d12.resultado()}.')
        elif opcion == 7:
            print(f'Al lanzar el dado d20, ha salido {d20.resultado()}.')
        elif opcion == 0:
            print('Ha salido del juego')
            break
        else:
            print('La opción indicada no es correcta')

    

