class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        print(f"{self.nombre} está jugando ")
        self.felicidad += 10
        self.salud -= 5
        self.energia -= 10
        self._mostrar_estado()

    def comer(self):
        print(f"{self.nombre} está comiendo ")
        self.felicidad += 5
        self.salud += 10
        self.energia += 15
        self._mostrar_estado()

    def curar(self):
        print(f"{self.nombre} está siendo curado ")
        self.salud += 20
        self.felicidad -= 5
        self._mostrar_estado()

    def _mostrar_estado(self):
        print(f"➡️ Estado de {self.nombre}: Salud={self.salud}, Felicidad={self.felicidad}, Energía={self.energia}\n")