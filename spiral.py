import turtle
screen = turtle.Screen()
draw = turtle.Turtle()
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(50):
  draw.forward(i*5)
  draw.right(90)
turtle.done()