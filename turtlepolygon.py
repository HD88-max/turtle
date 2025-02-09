import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(400,400)
sides = int(input("Enter sides: "))
length = int(input("Enter length: "))
angle = 360/sides
polygon = turtle.Turtle()
for i in range(sides):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()