import turtle

size = 100

turtle.pensize(2)

turtle.penup()
turtle.setpos(-300, 0)
turtle.pendown()

for count in range(0,5):
    for side_num in range(0, 4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()
    turtle.forward(size+10)
    turtle.pendown()
    size = size - 20

turtle.done()