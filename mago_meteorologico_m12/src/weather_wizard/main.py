"""
Punto de entrada para la aplicación Weather Wizard.
Organizado para la clase CS1400 - Universidad Weber.
"""

from weather_wizard.motor import obtener_clima_ciudad

def main():
    print("--- Bienvenido a Weather Wizard ---")
    
    ciudad = input("Introduce una ciudad (ej. London): ").strip()
    
    if not ciudad:
        print("Error: No ingresaste nada.")
        return

    try:
        resultado = obtener_clima_ciudad(ciudad)

        if isinstance(resultado, dict) and "error" in resultado:
            print(f"Ocurrió un error: {resultado['error']}")
        else:
            # Aquí es donde Pylance se quejaba. Ahora está limpio:
            print(f"\nClima en: {resultado['city']}")
            print(f"Temperatura: {resultado['temp']}°C")
            print(f"Condición: {resultado['condition']}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()