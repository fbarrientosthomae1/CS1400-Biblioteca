import math

# Crear una función para verificar si un número es un cuadrado perfecto
def es_cuadrado_perfecto(n):
    # TODO 1: Si el número es negativo, no es cuadrado perfecto.
    if n < 0:
        return False
    
    # Calcular la raíz cuadrada entera del número de forma segura
    return math.isqrt(n) ** 2 == n

# Entrada del usuario
num_usuario = int(input("¿Qué número te gustaría revisar si es cuadrado perfecto? "))

# Mostrar el resultado
if es_cuadrado_perfecto(num_usuario):
    print(f"El número {num_usuario} es un cuadrado perfecto.")
else:
    # TODO 2: Mensaje al usuario si NO es cuadrado perfecto. 
    print(f"El número {num_usuario} NO es un cuadrado perfecto.")

# TODO 3: ¿Cuál era el error?
# El error principal era el nombre de la variable en el bucle: 
# Tenías 'test_valores' arriba y 'test_values' (en inglés) en el for.

print("\nPruebas automáticas con varios valores:")
test_valores = [0, 1, 4, 9, 16, 25, 26, 27, 100, 101, -1, -4]

for num in test_valores: # Cambiado de test_values a test_valores
    resultado = es_cuadrado_perfecto(num)
    estado = "✅" if resultado else "❌"
    print(f"{estado} {num} {'es' if resultado else 'NO es'} un cuadrado perfecto.")