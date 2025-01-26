print("Hi! I am an integer adder.")
class Sum:
  def __init__(self, firstnum, secondnum, thirdnum):
    self.num1 = firstnum
    self.num2 = secondnum
    self.num3 = thirdnum
  def summing(self):
    self.result = 0
    if type(self.num1) == int:
      if type(self.num2) == int:
        if type(self.num3) == int:
          self.result = self.num1 + self.num2 + self.num3
          return self.result
        else:
          print("Error")
      else:
        print("Error")
    else:
      print("Error")
user = Sum(int(input("What is the first number? ")), int(input("What is the second number? ")), int(input("What is the third number? ")))
print("The sum is", user.summing())
