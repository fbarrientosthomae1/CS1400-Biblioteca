# --- Diaro de      Digital ---
import datetime
# Aqui tu funcion menu()
def menu():
    print("\n--- MI DIARIO PERSONAL ---")
    print("1. Escribir una nueva entrada")
    print("2. Leer el diario completo")
    print("3. Salir")
    return input("Selecciona una opción (1, 2 o 3): ")
while True:
    opcion = menu()

    #Aqui tu if/elif/elif/else statement con las opciones del menu
    if opcion == "1":
        # Entrada de datos
        pensamiento = input("¿Qué quieres escribir hoy?: ")
        
        # Puntos Extra: Obtener fecha y hora automática
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Guardar en archivo
        # 'a' significa "append" (añadir al final) para no borrar lo anterior
        with open("mi_diario.txt", "a", encoding="utf-8") as archivo:
            # Cada linea comienza con un guion como pide la tarea
            archivo.write(f"- [{ahora}] {pensamiento}\n")
        print("¡Entrada guardada con éxito!")

    elif opcion == "2":
        # Leer el archivo 
        print("\n--- LEYENDO TU DIARIO ---")
        try:
            with open("mi_diario.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                if contenido:
                    print(contenido)
                else:
                    print("El diario está vacío por ahora.")
        except FileNotFoundError:
            print("Aún no has creado el archivo del diario. ¡Escribe algo primero!")

    # Salir de tu ultimo elif con un break
    elif opcion == "3":
        print("Cerrando el diario. ¡Hasta luego!")
        break 
    
    # else solo para mostrar al usuario que no funciono lo que intentaron ingresar
    else:
        print(f"Error: La opción '{opcion}' no es válida. Intenta de nuevo.")
    # Entrada de datos
    # Guardar en archivo
    # Leer el archivo 