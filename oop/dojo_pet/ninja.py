from pet import Pet
class Ninja():
    def __init__(self,first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        print(f"{self.first_name} give {self.pet.name} {self.pet_food}")
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

pet = Pet("Pixie", "dog", "dance", 100, 50)
ninja = Ninja("Yaki", "Soba", pet, "cookie", "chicken" )

ninja.feed().walk().bathe()