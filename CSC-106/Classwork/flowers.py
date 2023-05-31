import turtle as t 

def flower(flower_radius):
    for x in range (0,6): 
        t.circle(flower_radius/2)
        t.left(60)

flower(50)