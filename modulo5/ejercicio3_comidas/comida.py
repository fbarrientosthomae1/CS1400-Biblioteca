"""
Este programa permite al usuario elegir una comida de una lista y muestra su país de origen.
Utiliza lógica condicional y normalización de texto.
"""

# TODO #1: Imprime un mensaje de bienvenida
print("Bienvenido al programa de comidas de Latinoamérica.")

# TODO #2: Muestra al usuario la lista de opciones
print("Opciones: tacos, arepas, ceviche, pupusas, empanadas")

# TODO #3: Guarda lo que el usuario escribió en una variable
eleccion = input("¿Qué comida quieres conocer? ")

# TODO #4: Convierte lo ingresado a minúsculas para evitar errores
comida = eleccion.lower()

# TODO #5: Estructura if / elif / else para verificar el origen
if comida == "tacos":
    print("Los tacos son típicos de México.")
elif comida == "arepas":
    print("Las arepas son tradicionales de Venezuela y Colombia.")
elif comida == "ceviche":
    print("El ceviche es el plato bandera de Perú.")
elif comida == "pupusas":
    print("Las pupusas son el plato nacional de El Salvador.")
elif comida == "empanadas":
    print("Las empanadas son populares en muchos países, especialmente en Argentina y Chile.")
else:
    # Mensaje de error si la opción no está en la lista
    print("Lo siento, esa comida no está en nuestra lista de opciones.")