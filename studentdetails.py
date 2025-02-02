class Person:
    def __init__(self, name1, name2):
        self.firstname = name1
        self.lastname = name2
    def display(self):
        print("Student name is {} {}.".format(self.firstname, self.lastname))
class Graduate(Person):
    def __init__(self, name1, name2, gradyear):
        self.gradyear = gradyear
        super().__init__(name1, name2)
student = Graduate("Alice", "Stevenson", 2024)
student.display()
print("He/She graduated in {}.".format(student.gradyear))