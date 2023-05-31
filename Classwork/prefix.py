def is_prefix(list1, list2): 
    
    for i in range(0,len(list1)):
        
        if list1[i] != list2[i]:
            return False 
        
    return True

print(is_prefix([1,2,3,7], [1,2,3,7,4,8,6,3]))
    

