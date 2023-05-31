# Draw a simple snowflake shape.
#
# Neil Daterao
# Winter 2022

import turtle as t 


#function that makes the "turtle.goto" command shorter, don't have to repeat penup and pendown
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


#function for snowflake that takes parameter for size and color
def snowflake(size, color):

    t.pensize(4)
    t.color(color)

    #loop to make snowflakes 
    for x in range (4):
        t.forward(size)
        t.backward(size*2)
        t.forward(size)
        t.left(45)


    t.right(135)


#go to various coordinates and draw snowflakes 

goto(-200,50)
snowflake(50, "purple")
goto(-75,-100)
snowflake(80, "navy")
goto(100,-70)
snowflake(30, "light blue")
goto(300,40)
snowflake(40, "blue")
