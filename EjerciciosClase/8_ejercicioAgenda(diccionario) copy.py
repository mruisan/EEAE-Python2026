# Crea un programa que gestione una agenda de contactos USANDO DICCIONARIO donde:
#  - La clave es el nombre de la persona
#  - El valor es su número de teléfono
# El programa debe permitir:
# - Añadir un contacto nuevo
# - Buscar un contacto por nombre
# - Eliminar un contacto
# - Mostrar todos los contactos (quien quiera sufrir, que los devuelva ordenados alfabéticamente)

agenda = {
    "Sauca" : "123456789"
}

def nuevo_contacto():
    nombre = input("Introduzca el nombre del contacto: ")
    telefono = input("Introduzca el número de teléfono: ")
    agenda[nombre] = telefono
    print("Contacto añadido")

def buscar_contacto():
    nombre = input("Introduzca el nombre a buscar: ")

    # Una manera posible (Case sensitive)
    """
    if nombre in agenda:
        print(nombre, ": ", agenda[nombre])
    else:
        print("Contacto no encontrado")
    """

    # Otra manera más (que no es case sensitive)
    """
    for i in agenda:
        if i.lower() == nombre.lower():
            print(i, ": ", agenda[i])
        else:
            print("Contacto no encontrado")
    """

    # Otra manera usando el método get
    print(agenda.get(nombre, "Contacto no encontrado"))

def eliminar_contacto():
    nombre = input("Introduzca el contacto a eliminar: ")
    try:
        del agenda[nombre]
        print("Contacto eliminado")
    except:
        print("El contacto no existe")

def mostrar_contactos():
    for i in sorted(agenda):
        print(f"{i}: {agenda[i]}")