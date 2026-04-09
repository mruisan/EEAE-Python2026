
# Ejercicio 8: Validación de contraseña
# Diseña una clase Validador con un atributo para una contraseña.
# Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.

class Validador:
    def __init__(self,contraseña):
        self.contraseña=contraseña

    def comprobar(self):
        mayusculas= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        numeros= '1234567890'
        long= 0
        mayu= 0
        nume= 0
        if len(self.contraseña) >= 8:
            long += 1
        for i in self.contraseña:
            if i in mayusculas:
                mayu += 1
            elif i in numeros:
                nume += 1
        if long != 0 and mayu !=0 and nume != 0 :
            print('La contraseña SI cumple con los requisitos')
        else:
            print('La contraseña NO cumple con los requisitos')


contraseña_1= Validador('Contraseña')
contraseña_2= Validador('123Password')

if __name__ == "__main__":
     contraseña_1.comprobar()
     contraseña_2.comprobar()