from persona import Persona
from tamagotchi import Tamagotchi

if __name__ == "__main__":
    mi_tamagotchi = Tamagotchi("Pixel", "Rojo")
    persona = Persona("Francis", "Fernandez", mi_tamagotchi)

    persona.darle_comida()
    persona.curarlo()
    persona.jugar_con_tamagotchi()