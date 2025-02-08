class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}.")
    def sound(self):
        print("Bark!")
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def info(self):
        print(f"My name is {self.name} and my age is {self.age}.")
    def sound(self):
        print("Meow!")
cat = Cat("Alice", 9)
dog = Dog("Lyla", 13)
for animal in (cat, dog):
    animal.info()
    animal.sound()    