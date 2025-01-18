import random
print("Welcome to the Quiz Competition!")
print("In here, You have to choose any number out of the 5 options of which I am thinking of.")
numbers = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
answer = numbers[random.randint(0,4)]
print("Your options are", numbers)
userguess = int(input("What is your guess?"))
if userguess > answer:
  print("No. Your guess was higher than what I thought!")
  print("The answer was", answer)
elif userguess < answer:
  print("No. Your guess was lower than what I thought!")
  print("The answer was", answer)
else:
  print("You got it right!")