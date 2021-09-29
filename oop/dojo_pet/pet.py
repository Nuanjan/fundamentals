class Pet:
    def __init__(self, name, pet_type, tricks, health, energy):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    def sleep(self):
        self.energy += 25
        print(f"Now {self.name} has: {self.energy} energy!")
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Now {self.name} has: {self.energy} energy and {self.health} health!")
    def play(self):
        self.health += 5
        print(f"Now {self.name} has: {self.health} health!")
    def noise(self):
        if self.pet_type == "dog":
            print("woof woof!")
        elif self.pet_type == "cat":
            print("meow meow~")
        else:
            print("I can't make sound")
