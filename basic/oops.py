class Animal:
    life = "10 years"

    def __init__(self, name, species):
        self.name = name
        self.species = species


class Cat(Animal):

    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color
        self.__kind = 11


animal = Animal("cat", "walking")
cat = Cat("cat", "walking", "black")

print(animal.name, animal.species)
print(animal.__class__.life)
print(Animal.life)

print(cat.name, cat.species, cat.color)
