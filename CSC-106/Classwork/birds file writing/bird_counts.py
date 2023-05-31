#Neil Daterao

#
# Given a file that lists the names of all birds that have been
# observed over a certain period of time in a certain geographic area
# create a dictionary that represents how often each bird type was
# observed. (The file lists one bird name per line.)

def get_bird_counts(filename):
    file = open(filename, 'r')
   
    birdcount = {}

    for line in file:
        bird = line.strip()
        
        if bird in birdcount: 
            birdcount[bird] += 1
        else:
            birdcount[bird] = 1
    
    
    
    file.close()
    return birdcount 

def show_bird_counts(bird_counts):
    for bird,count in bird_counts.items():
        print(bird + ":", count)

def main():
    
    bird_counts = get_bird_counts("/home/dateraon/Desktop/Coding Projects/Classwork/birds file writing/birds.txt")
    
    show_bird_counts(bird_counts)

main()
