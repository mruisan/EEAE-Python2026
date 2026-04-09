
# Ejercicio 12: Contador de vocales
# Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
# Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.

class AnalizadorTexto:
    def __init__(self,texto):
        self.texto=texto
        self.vocales='aeiouAEIOU'

    def contar(self):
        contador= 0
        for i in self.texto:
            if i in self.vocales:
                contador+=1
        return (contador)       
    
frase=AnalizadorTexto(str(input('Indica tu frase: ')))

if __name__ == "__main__":
    print(f'La frase introducida tiene {frase.contar()} vocales.')




