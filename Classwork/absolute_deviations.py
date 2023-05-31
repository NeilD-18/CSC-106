def average(list):
    sum = 0 
    
    for num in list: 
        sum = sum + num 
    
    return (sum/(len(list)))

def abs_dev(list):
    mean = average(list)

    dev_list = []

    for num in list:
        temp = num - mean 
        dev_list.append(temp)
    
    return dev_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(abs_dev(list))
