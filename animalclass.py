from abc import ABC
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I am a human. I can run and walk.")
class Dog(Animal):
    def move(self):
        print("I am a dog. I can bark and also run like humans.")
class Fish(Animal):
    def move(self):
        print("I am a fish. I live in water and I swim.")
class Frog(Animal):
    def move(self):
        print("I am a Frog. I am an amphibian(lives in both land and water) and I use my webbed feet to jump.")
object = Human()
object.move()
object = Dog()
object.move()
object = Fish()
object.move()
object = Frog()
object.move()