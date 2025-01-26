class employment:
    company = input("What company do you work in?")
    def __init__(self, name, age):
        print("Hi! I work in", self.company)
        self.name = name
        self.age = age
        print("Hi! My name is {} and my age is {}.".format(self.name, self.age))
    def __del__ (self):
        print("Employee got fired.")
employee = employment("Zinat", 33)
del employee