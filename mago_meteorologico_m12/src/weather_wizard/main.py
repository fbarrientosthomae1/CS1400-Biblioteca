from weather_wizard.motor import obtener_clima_ciudad

def main():
    print("--- Bienvenido a Weather Wizard ---")
    ciudad = input("Introduce una ciudad (ej. London): ").strip()
    
    if not ciudad:
        print("Error: No ingresaste nada.")
        return

    resultado = obtener_clima_ciudad(ciudad)

    if "error" in resultado:
        print(f"Ocurrió un error: {resultado['error']}")
    else:
        print(f"\nClima en {resultado['city']}:")
        print(f"- Temperatura: {resultado['temp']}°C")
        print(f"- Condición: {resultado['condition']}")

if __name__ == "__main__":
    main(Ne