list = [-5,3,10,-2,-6,10,8]
list1 = [2,4,5,7]
def neg_num(list): 
    for num in list:
        if num < 0: 
            return True 
    return False 

print(neg_num(list))
print(neg_num(list1))