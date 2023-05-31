#Neil Daterao

#Program that draws circles with different size and colors 

import turtle as t

#circle defintion that takes both size and color as parameters 
def circle(size, color):
    t.pencolor(color) 
    t.circle(size)

#draw the five circles with different colors 
circle(10, "yellow")
circle(20, "orange")
circle(30, "red")
circle(40,"blue")
circle(50, "green")
