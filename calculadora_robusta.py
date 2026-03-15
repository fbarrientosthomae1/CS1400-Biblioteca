def calculadora_segura():
    print("\n--- Bienvenido a la Calculadora Robusta ---")
    
    while True:
        try:
            # Solicitar datos
            n1 = float(input("Ingresa el primer número: "))
            n2 = float(input("Ingresa el segundo número: "))
            op = input("Operación (+, -, *, /): ")

            # Validar operación (Regla de negocio)
            if op not in ['+', '-', '*', '/']:
                # TODO: Lanza (raise) una excepción ValueError
                raise ValueError("Operador no válido")

            # Realizar cálculos
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                resultado = n1 / n2

            print(f"✅ Resultado: {resultado}")
            break # Rompe el bucle si todo salió bien

        # --- MANEJO DE ERRORES ---
        
        # Error cuando el usuario ingresa letras
        except ValueError as e:
            if str(e) == "Operador no válido":
                print(f"Error de entrada: {e}")
            else:
                print("Error: Solo se admiten números.")

        # Error de división por cero
        except ZeroDivisionError:
            print("Error: No puedes dividir un pastel entre cero personas.")

        except Exception as e:
            print(f"Algo salió muy mal: {e}")
        
        finally:
            # Mensaje que aparece SIEMPRE
            print("Intento de cálculo finalizado.")

calculadora_segura()