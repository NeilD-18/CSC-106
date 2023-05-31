list = [5,10,15,20]

def average(list):
    sum = 0 
    
    for num in list: 
        sum = sum + num 
    
    return (sum/(len(list)))

print(average(list))
