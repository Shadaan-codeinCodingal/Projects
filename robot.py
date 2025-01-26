class robot:
  def __init__(self, name, age):
      self.name = name
      self.age = age
robo1 = robot("Tom", 15)
robo2 = robot("Jerry", 12)
print("Hi! My name is {} and I am {} years old.".format(robo1.name, robo1.age))
print("Hi! My name is {} and I am {} years old.".format(robo2.name, robo2.age))
