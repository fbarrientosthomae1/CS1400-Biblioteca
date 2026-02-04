"""Este programa debe darle al usuario la opcion de elegir una comida de una lista.
El codigo asegura que lo ingresado sea legible (en minusculas) y lo compara con una lista uusando logica if/else"
Al final, muestra un mensaje explicando de donde es originaria esa comida
"""

# TODO #1: 
#Imprime un mensaje de bienvenida al programa de comidas de latinoamérica.

# TODO #2: 
#Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.

# TODO #3:
#Guarda lo que el usuario escribió en una variable llamada "comida".

# TODO #4: 
#Convierte lo ingresado a minúsculas para asegurar la comparación correcta.

# TODO #5:
#Usa una estructura if / elif / else para verificar la comida elegida.
#Imprime un mensaje con el país de origen para cada comida.

## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
""" 

print("Bienvenido al programa de comidas de Latinoamérica.")
print("Opciones: tacos, arepas, ceviche, pupusas, empanadas")
comida = input ("Elique una comida y te dire de donde es:")
comida = comida.lower()
if comida == "tacos":
    print( "Los tacos son típicos de México.")
elif comida == "arepas":
    print("Las arepas son típicas de Venezuela y Colombia")
elif comida == "ceviche":
    print( "El ceviche es típico de Perú.")
elif comida == "pupusas":
    print("Las pupusas son típicas de El Salvador.")
elif comida == "empanadas":
    print("Las empanadas son típicas de Argentina.")
else:
    print("Lo siento, esa comida no se de qué país es.")
