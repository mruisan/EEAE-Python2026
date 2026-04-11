
# Ejercicio 11: Gestión de cuentas bancarias
# Crea una clase CuentaBancaria con atributos para titular y saldo.
# Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar
# saldos negativos.

class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo

    def deposito(self,ingreso):
        try:
            if ingreso < 0:
                raise ValueError ('La cantidad a ingresar tiene que ser positiva.')
            else:
                self.saldo+=ingreso
                return f'\nTras el ingreso tienes un saldo de {self.saldo}€.\n'
        except ValueError as e:
            return e
    
    def retirar(self,retirada):
        try:
            if self.saldo < retirada:
                raise ValueError ('Saldo insuficiente, no puedes retirar tanto dinero.')
            elif retirada < 0:
                raise ValueError ('La cantidad a retirar tiene que ser positiva.')
            else:
                self.saldo-=retirada
                return f'\nTras retirada tienes un saldo de {self.saldo}€.\n'
        except ValueError as e:
            return e
    
    def consulta(self):
        return f'\nEl usuario {self.titular} tiene un saldo actual de {self.saldo}€.\n'

cuenta_1= CuentaBancaria('Manuel Ruiz',500)

if __name__ == "__main__":

    while True:
        print('MENÚ\n')
        print('Pulsa 1 para ingresar dinero')
        print('Pulsa 2 para retirar dinero')
        print('Pulsa 3 para consultar la cuenta')
        print('Pulsa 0 para salir')
        opcion= int(input('Marca una opción: '))
        if opcion == 1:
            print(cuenta_1.deposito(int(input('Indique la cantidad a ingresar: '))))
        if opcion == 2:
            print(cuenta_1.retirar(int(input('Indique la cantidad a retirar: '))))
        if opcion == 3:
            print(cuenta_1.consulta())
        if opcion == 0:
            break


