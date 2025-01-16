import turtle
screen = turtle.Screen()
screen.bgcolor("Red")
screen.setup(1000, 1000)
screen.title("Codingal - L6 - ACP - Shapes(Equilateral Triangle and Hexagon)")
drawer = turtle.Turtle()
for i in range(3):
  drawer.forward(200)
  drawer.left(120)
drawer.penup()
drawer.backward(150)
drawer.pendown()
for j in range(6):
  drawer.backward(100)
  drawer.right(60)
turtle.done()