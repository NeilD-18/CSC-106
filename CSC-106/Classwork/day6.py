import turtle as t 
def circle():
    t.pendown()
    t.pensize(15)
    t.circle(50)
    t.penup()

def square():
    t.pendown()
    t.pensize(15)
    t.pencolor("green")
    for x in range (4):
        t.forward(100)
        t.left(90)
    t.penup()

def triangle():
    t.pendown()
    t.pensize(15)
    t.color("gold")
    t.fillcolor("purple")
    t.begin_fill()
    for x in range(3):
        t.forward(100)
        t.right(-120)
    t.end_fill()





def draw(): 
    i=0 
    x=0
    y=0 
    while(i<9): 
        t.goto(x,y)
        square()
        x = x + 100
        if (x == 300): 
            x = 0 
            square()
            y = y + 100
    i = i + 1
    

draw()


t.done()