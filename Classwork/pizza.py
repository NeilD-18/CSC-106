import math as m

def circle_area(radius):
    area = m.pi * (radius ** 2)
    return area 

def pizza_cost(diameter, price):
    area = circle_area(diameter/2)
    cpi = price / area 
    return cpi 

print(pizza_cost(15, 25))