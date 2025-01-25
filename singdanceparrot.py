class parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def singing(self, song):
        return "{} is singing {}.".format(self.name, song)
    def dancing(self):
        return "{} is dancing.".format(self.name)
alice = parrot("Alice", 13)
print(alice.singing("Happy"))
print(alice.dancing())