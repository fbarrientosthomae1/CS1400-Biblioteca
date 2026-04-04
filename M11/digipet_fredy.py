import random

class DigiPet:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.comida = 100
        self.salud = 100
        self.vivo = True

    def mostrar_estado(self):
        print(f"\n--- ESTADO DE {self.nombre.upper()} ---")
        print(f"Felicidad: {self.felicidad} | Comida: {self.comida} | Salud: {self.salud}")
        print("--------------------------------")

    def envejecer(self):
        # Simula el paso del tiempo bajando los niveles en cada turno
        self.felicidad -= 5
        self.comida -= 7
        self.salud -= 3
        self.verificar_muerte()

    def alimentar(self):
        print(f"\nLe das de comer a {self.nombre}. ¡Está delicioso!")
        self.comida += 20
        if self.comida > 110: self.comida = 110 # Límite máximo

    def jugar(self):
        print(f"\nJuegas con {self.nombre}. ¡Está muy feliz!")
        self.felicidad += 15
        self.comida -= 5

    def pasear(self):
        print(f"\nSacas a {self.nombre} al parque. El ejercicio le hace bien.")
        self.salud += 10
        self.felicidad += 10
        self.comida -= 10

    def verificar_muerte(self):
        if self.comida <= 0 or self.felicidad <= 0 or self.salud <= 0:
            self.vivo = False
            print(f"\nOh no... {self.nombre} ha muerto por descuido. :( ")

# --- LÓGICA DEL JUEGO ---
def menu():
    nombre_pet = input("¿Cómo se llamará tu DigiPet? ")
    mi_mascota = DigiPet(nombre_pet)

    while mi_mascota.vivo:
        mi_mascota.mostrar_estado()
        print("1. Jugar")
        print("2. Alimentar")
        print("3. Pasear")
        print("4. Salir")
        
        opcion = input("\n¿Qué te gustaría hacer hoy? ")

        if opcion == "1":
            mi_mascota.jugar()
        elif opcion == "2":
            mi_mascota.alimentar()
        elif opcion == "3":
            mi_mascota.pasear()
        elif opcion == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")

        # El tiempo pasa después de cada acción
        mi_mascota.envejecer()

if __name__ == "__main__":
    menu()