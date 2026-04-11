# Practicando lógica booleana en Python: "and", "or" y "not"

# Inicialización de Valores
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Condición: 18 años o más Y tiene permiso
puede_salir_estricto = edad >= 18 and tiene_permiso
print(f"¿Puede salir bajo la regla estricta (18+ y permiso)?: {puede_salir_estricto}")


# TODO 2: Usa una expresión booleana con "or"
# Condición: Es fin de semana O tiene permiso
puede_salir_flexible = es_finde or tiene_permiso
print(f"¿Puede salir bajo la regla flexible (Finde o permiso)?: {puede_salir_flexible}")


# TODO 3: Usa una expresión booleana con "not"
# Condición: De ninguna manera tiene permiso
no_tiene_permiso = not tiene_permiso
print(f"¿Es verdad que NO tiene permiso?: {no_tiene_permiso}")


# TODO 5: Escribe tu propia condición
# Situación: ¿Puede jugar videojuegos? 
# Condición: Si es fin de semana O (si ha terminado su tarea Y tiene permiso)
# Nota: Aquí usamos paréntesis para agrupar lógica, igual que en matemáticas.
termino_tarea = True
puede_jugar = es_finde or (termino_tarea and tiene_permiso)

print(f"¿Puede jugar videojuegos hoy?: {puede_jugar}")