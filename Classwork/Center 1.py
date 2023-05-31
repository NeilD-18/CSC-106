#used in reborg (not built in functions)

def go(x):
    i = 0 
    while(i<x):
      move()
      i = i+1
        
def turn_right():
    for x in range(3):
        turn_left() 
        

def square(r):  
    j = 0
    while (j<4):
        go(r)
        turn_left()
        j = j+1 

def stepup(x):
    i = 0
    while (i<x):
        turn_left()
        go(1)
        turn_right()
        go(2)
        i = i + 1

def stepdown(x):
    i = 0
    while (i<x):
        go(2)
        turn_left()
        go(1)
        turn_right()
        j = j+1

def navigate(x):
   i = 0
   while (i<x):
        go(3)       
        turn_left() 
        go(3)       
        turn_right()
        
        if front_is_clear(): 
            go(1) 
            turn_right() 
            
        i = i+1
        
def navigate1():
    i = 0
    while (i<1):
        if right_is_clear():
            turn_right()
            go(1)
        elif front_is_clear():
            go(1)
        elif wall_on_right():
            turn_left()
    
        if at_goal():
            break
            
        
        
    


think(0)        
navigate1()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
help()
