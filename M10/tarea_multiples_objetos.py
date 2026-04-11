import random

# ==========================================
# PARTE 1: DEFINICIÓN DE LA CLASE (El "Cerebro")
# ==========================================
class Player:
    # Método constructor init
    def __init__(self):
        self.score = 0
        self.totalRoll = 0

    # Método para lanzar dados
    def roll(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        self.totalRoll = dado1 + dado2
        return self.totalRoll

    def __str__(self):
        return "Score: " + str(self.score)

    def addToScore(self):
        self.score += 1


# ==========================================
# PARTE 2: EL CUERPO DEL JUEGO (Debajo de la clase)
# ==========================================
# Aquí creas las instancias
player1 = Player()
player2 = Player()

opcion = ""
while opcion.lower() != "quit":
    # Llamamos a los métodos que creamos arriba
    p1_tiro = player1.roll()
    p2_tiro = player2.roll()
    
    print(f"\nJugador 1 lanzó: {p1_tiro}")
    print(f"Jugador 2 lanzó: {p2_tiro}")
    
    # Lógica de la ronda
    if p1_tiro > p2_tiro:
        player1.addToScore()
        print(">>> Punto para el Jugador 1")
    elif p2_tiro > p1_tiro:
        player2.addToScore()
        print(">>> Punto para el Jugador 2")
    else:
        print(">>> Empate en esta ronda")
        
    print(f"Marcador: P1[{player1}] | P2[{player2}]")
    opcion = input("Enter para seguir o 'quit' para salir: ")

# Lógica final fuera del bucle
print("\n--- RESULTADO FINAL ---")
if player1.score > player2.score:
    print(f"¡GANASTE! {player1.score} a {player2.score}")
elif player2.score > player1.score:
    print(f"PERDISTE. El oponente ganó {player2.score} a {player1.score}")
else:
    print("Empate final.")