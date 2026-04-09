
# Ejercicio 6: Ordenar una lista
# Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
# Luego, intégrala como método en una clase Ordenador.

def ordenar(lista):
    for i in range (len(lista)):
        for j in range (0,len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

class Ordenador:
    def __init__(self,lista):
        self.lista=lista

    def metodo_ordenar(self):
        return ordenar(self.lista)

prueba_1=Ordenador([3,6,23,1,9,14,45,98])

if __name__ == "__main__":
    print(prueba_1.metodo_ordenar())