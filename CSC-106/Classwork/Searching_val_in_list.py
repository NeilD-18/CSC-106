#Iterate through list I. If index is equal to target value, return true, else, keep iterating through the list 

#If target value is greater than the last value of the list or smaller than the first value of the list, return False, else iterate through the list and if the index is equal to the target value, return True


given_list = [10,3,13,11,5,20]
sorted_list = [3,5,10,11,13,20]
target_value = 11

def test(target_value,list):
    
    for i in range(len(list)):
        if list[i] == target_value:
            return True
    return False 

def sorted_test(target_value, list):
    if target_value < list[0] or target_value > list[len(list-1)]:
        return False
    else: 
        for i in range(len(list)):
            if list[i] == target_value:
                return True
        return False 

print(test(5,given_list))