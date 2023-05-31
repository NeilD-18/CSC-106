list = [2,4,7,8,2,5,6,2,8,10]

def matches(list, value): 
    count = 0
    for num in list: 
        if num == value:
            count += 1
    
    return count

print(matches(list, 2))