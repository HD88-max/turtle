import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(400,400)
sides = 5
length = int(input("Enter length: "))
angle = 144
star = turtle.Turtle()
for i in range(sides):
    star.forward(length)
    star.right(angle)
turtle.done()