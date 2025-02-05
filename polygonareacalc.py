from abc import ABC, abstractmethod
import math
print("Hi! I am a Polygon calculator. Choose any of the following shapes. 1. Triangle 2. Square 3. Rectangle 4. Circle 5. Regular Pentagon 6. Regular Hexagon")
class Shapes:
  def __init__(self, sides):
    self.sides = sides
  def calculate(self):
    pass
class Triangle(Shapes):
  def calculate(self):
    if self.sides[0]*self.sides[1]/2 - int(self.sides[0]*self.sides[1])/2 == 0:
      print("The area of a triangle is", int(self.sides[0]*self.sides[1])/2)
    else:
      print("The area of a triangle is", ((self.sides[0]*self.sides[1])/2))
class Squares(Shapes):
  def calculate(self):
    if self.sides**2 - int(self.sides**2) == 0:
      print("The area of a square is", int(self.sides*self.sides[1])/2)
    else:
      print("The area of a square is", (self.sides*self.sides[1])/2)
class Rectangle(Shapes):
  def calculate(self):
    if self.sides[0]*self.sides[1] - int(self.sides[0]*self.sides[1]) == 0:
      print("The area of a rectangle is", int(self.sides[0]*self.sides[1]))
    else:
      print("The area of a rectangle is", (self.sides[0]*self.sides[1]))
class Circle(Shapes):
  def calculate(self):
    if self.sides**2*math.pi - int(self.sides**2*math.pi ) == 0:
      print("The area of a circlee is", int(self.sides**2*math.pi ))
    else:
      print("The area of a triangle is", (self.sides**2*math.pi ))
class RegularPentagon(Shapes):
  def calculate(self):
    if 1/4*math.sqrt(5 + 2*math.sqrt(5))*self.sides**2 - int(1/4*math.sqrt(5 + 2*math.sqrt(5))*self.sides**2) == 0:
      print("The area of a triangle is", int(1/4*math.sqrt(5 + 2*math.sqrt(5))*self.sides**2))
    else:
      print("The area of a triangle is", (1/4*math.sqrt(5 + 2*math.sqrt(5))*self.sides**2))
class RegularHexagon(Shapes):
  def calculate(self):
    if 3*math.sqrt(3)/2*self.sides**2 - int(3*math.sqrt(3)/2*self.sides**2) == 0:
      print("The area of a hexagon is", int(3*math.sqrt(3)/2*self.sides**2))
    else:
      print("The area of a hexagon is", (3*math.sqrt(3)/2*self.sides**2))
choice = int(input("Enter your choice: "))
sides = 0
while choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
  if choice == 1 or choice == 3:
    sides = [int(input("Enter length of base: ")), int(input("Enter length of height: "))]
  elif choice == 4:
    sides = int(input("Enter radius: "))
  else:
    sides = int(input("Enter side length: "))
  
  if choice == 1:
    user = Triangle(sides)
    user.calculate()
  elif choice == 2:
    user = Squares(sides)
    user.calculate()
  elif choice == 3:
    user = Rectangle(sides)
    user.calculate()
  elif choice == 4:
    user = Circle(sides)
    user.calculate()
  elif choice == 5:
    user = RegularPentagon(sides)
    user.calculate()
  else:
    user = RegularHexagon(sides)
    user.calculate()
  break
