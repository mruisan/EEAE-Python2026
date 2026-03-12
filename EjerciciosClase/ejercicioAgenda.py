import json

def cargar_contactos():
    with open("resources/json/contactos.json", "r") as contactos_aqui:
        diccionario_temporal_contactos = json.load(contactos_aqui)
        return diccionario_temporal_contactos

def nuevo_contacto(pollasnegras):
    nombre = input("Introduzca el nombre del contacto: ")
    telefono = input("Introduzca el número de teléfono: ")
    pollasnegras[nombre] = telefono
    print("Contacto añadido")

def guardar_cambios(loquevienedefuera):
    with open("resources/json/contactos.json", "w") as otrapollanegra:
        json.dump(loquevienedefuera, otrapollanegra, indent=4)
