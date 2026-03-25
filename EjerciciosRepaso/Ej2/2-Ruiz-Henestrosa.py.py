
# Ejercicio 2: Contador de palabras
# Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
# Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.

def cadena(texto):
    contador= texto.split()
    return len(contador)

class Texto:
    def __init__(self,texto):
        self.contenido=texto
    def metodo(self):
        return cadena(self.contenido)

frase_1= Texto("hola mundo")
frase_2= Texto("Contador de palabras en un texto")

if __name__ == "__main__":
    print(frase_1.metodo())
    print(frase_2.metodo())

