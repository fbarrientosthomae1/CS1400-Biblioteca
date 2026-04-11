import math

# Función principal
def es_cuadrado_perfecto(n):
    if n < 0:
        return False
    # math.isqrt devuelve la raíz cuadrada redondeada hacia abajo como entero
    return math.isqrt(n) ** 2 == n

# --- SECCIÓN EXTRA OPCIONAL ---
def imprimir_cuadrados_hasta(limite):
    """Imprime todos los cuadrados perfectos desde 0 hasta el límite."""
    print(f"\nCuadrados perfectos hasta el {limite}:")
    cuadrados = []
    for i in range(limite + 1):
        if es_cuadrado_perfecto(i):
            cuadrados.append(i)
    print(cuadrados)

# Entrada del usuario
num_usuario = int(input("¿Qué número te gustaría revisar? "))

# Mostrar el resultado
if es_cuadrado_perfecto(num_usuario):
    print(f"✅ El número {num_usuario} es un cuadrado perfecto.")
else:
    print(f"❌ El número {num_usuario} NO es un cuadrado perfecto.")

# Ejecutar la función extra
imprimir_cuadrados_hasta(num_usuario)

# Pruebas automáticas (TODO 3 Corregido)
print("\n--- Pruebas automáticas de validación ---")
test_valores = [0, 1, 4, 9, 16, 25, 26, 27, 100, 101, -1, -4]

for num in test_valores:
    resultado = es_cuadrado_perfecto(num)
    estado = "✅" if resultado else "❌"
    print(f"{estado} {num} {'es' if resultado else 'NO es'} un cuadrado perfecto.")