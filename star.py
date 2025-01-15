import turtle
turtle.Screen().bgcolor("Red")
screen = turtle.Screen()
screen.setup(400, 300)
drawer = turtle.Turtle()
for i in range(3):
   drawer.forward(100)
   drawer.left(120)
drawer.penup()
drawer.left(90)
drawer.forward(50)
drawer.pendown()
drawer.right(90)
for i in range(3):
   drawer.forward(100)
   drawer.right(120)
turtle.done()   