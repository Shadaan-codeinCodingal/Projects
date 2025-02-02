class Person:
    def __init__(self, idnum, name):
        self.idnumber = idnum
        self.name = name
    def display(self):
        print("Employee name is {} and his/her ID number is {}". format(self.name, self.idnumber))
class Employee(Person):
    def __init__(self, idnum, name, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, idnum, name)
employee = Employee(5763819023, "Farhaj Rehana", 32000, "Intern")
employee.display()
print("Employee's salary is {} and she is a {}.".format(employee.salary, employee.post))