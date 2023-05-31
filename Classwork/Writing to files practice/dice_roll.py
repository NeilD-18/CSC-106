import random as r 

def create_dice_roll(filename): 
    file = open(filename, "w")

    for x in range(1,1001): 
        val = r.randint(1,6)
        output = str(x) + ":" + " " + str(val)
        file.write(output)
        file.write("\n")

    file.close()

def read_dice_roll(filename): 
    file = open(filename, "r")
    roll_count = {}
    for line in file: 
        line = line.strip()
        [test,roll] = line.split(":")
        roll = roll.strip()
        
        if roll in roll_count: 
            roll_count[roll] += 1 

        else:
            roll_count[roll] = 1
    
    print("Number of 1's:", roll_count["1"])
    print("Number of 2's:", roll_count["2"])
    print("Number of 3's:", roll_count["3"])
    print("Number of 4's:", roll_count["4"])
    print("Number of 5's:", roll_count["5"])
    print("Number of 6's:", roll_count["6"])
        

        





read_dice_roll("dice_roll.txt")