class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
bird1 = parrot("Alice", 13)
bird2 = parrot("Bella", 21)
print("{} is a {}".format(bird1.name, bird1.species))
print("{} is also a {}".format(bird2.name, bird2.species))
print("{} is {} years old".format(bird1.name, bird1.age))
print("{} is {} years old".format(bird2.name, bird2.age))