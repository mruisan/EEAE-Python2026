
# Ejercicio 7: Registro de productos
# Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
# Añade un método que calcule el valor total del inventario (precio × cantidad).

class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre= nombre
        self.precio= precio
        self.cantidad= cantidad

    def calculo(self):
        stock= self.precio * self.cantidad
        return stock

producto_1= Producto('PC',1200,10)
producto_2= Producto('TV',700,12)
producto_3= Producto('Impresora',70,15)
inventario=[producto_1,producto_2,producto_3]

if __name__ == "__main__":
     print(producto_1.calculo())

     for i in inventario:
         print(f'El producto {i.nombre}, tiene un valor en el inventario de {i.calculo()} Euros.')
