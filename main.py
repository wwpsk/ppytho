import random

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.hunger = random.randint(0, 10)
        self.energy = random.randint(0, 10)

    def play(self):
        self.hunger += 2
        self.energy -= 1
        self.__update_state()

    def feed(self):
        self.hunger -= 3
        self.energy += 2
        self.__update_state()

    def sleep(self):
        self.hunger += 1
        self.energy += 3
        self.__update_state()

    def __update_state(self):
        if self.hunger < 0:
            self.hunger = 0
        if self.hunger > 10:
            self.hunger = 10
        if self.energy < 0:
            self.energy = 0
        if self.energy > 10:
            self.energy = 10

    def __str__(self):
        return f"Cat '{self.name}': Breed={self.breed}, Hunger={self.hunger}, Energy={self.energy}"

cat1 = Cat("Fluffy", "Persian")
cat2 = Cat("Whiskers", "Siamese")

print(cat1)
print(cat2)

cat1.feed()
cat1.play()
cat2.play()
cat2.sleep()

print(cat1)
print(cat2)