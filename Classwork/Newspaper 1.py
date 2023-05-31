def go(x):
    i = 0 
    while(i<x):
      move()
      i = i+1
        
def turn_right():
    for x in range(3):
        turn_left() 
        
#square 
def square(r):  
    j = 0
    while (j<4):
        go(r)
        turn_left()
        j = j+1 
        
think(100)       
take()        
        
i = 0 
while (i<3):
    turn_left()
    go(1)
    turn_right()
    go(2)
    i = i + 1

put()
take("token")
turn_left()
turn_left() 

j=0 
while (j<3):
    go(2)
    turn_left()
    go(1)
    turn_right()
    j = j+1


    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
