import random

# Definición de la Clase Player
class Player:
    def __init__(self, nombre):
        """Constructor: Inicializa el nombre, vida y fuerza."""
        self.nombre = nombre
        self.vida = 100
        self.fuerza = 0

    def setStrength(self):
        """Genera un número aleatorio para la fuerza del ataque."""
        self.fuerza = random.randint(1, 20)
        return self.fuerza

    def receiveDamage(self, puntos_daño):
        """Resta el daño recibido de los puntos de vida."""
        self.vida -= puntos_daño
        if self.vida < 0:
            self.vida = 0

# --- Lógica Principal del Programa ---
heroe = Player("Spidey")
villano = Player("Doc Ock")

print(f"Puntos de vida de {heroe.nombre}: {heroe.vida}")
print(f"Puntos de vida de {villano.nombre}: {villano.vida}\n")

continuar = ""
while heroe.vida > 0 and villano.vida > 0:
    print(f"¡{heroe.nombre}, es tu turno!")
    accion = input("Presiona 'h' para golpear, 'q' para salir: ").lower()

    if accion == 'q':
        break
    
    if accion == 'h':
        # Determinar fuerza de ambos
        f_heroe = heroe.setStrength()
        f_villano = villano.setStrength()
        
        if f_heroe > f_villano:
            daño = f_heroe - f_villano
            villano.receiveDamage(daño)
            print(f"Fuerza de {heroe.nombre}: {f_heroe}, Fuerza de {villano.nombre}: {f_villano}.")
            print(f"{villano.nombre} tiene {daño} puntos de daño.")
        elif f_villano > f_heroe:
            daño = f_villano - f_heroe
            heroe.receiveDamage(daño)
            print(f"Fuerza de {heroe.nombre}: {f_heroe}, Fuerza de {villano.nombre}: {f_villano}.")
            print(f"{heroe.nombre}, tienes {daño} puntos de daño.")
        else:
            print("¡Ambos chocaron con la misma fuerza! Nadie recibe daño.")

        # Mostrar estado actual
        print(f"Puntos de vida de {heroe.nombre}: {heroe.vida}")
        print(f"Puntos de vida de {villano.nombre}: {villano.vida}\n")

# --- Fin del Juego ---
print("¡Buena batalla!")
if heroe.vida > villano.vida:
    print(f"¡{heroe.nombre} gana esta ronda!")
elif villano.vida > heroe.vida:
    print(f"¡{villano.nombre} gana esta ronda!")
else:
    print("¡Fue un empate técnico!")

print("¡Gracias por jugar!")