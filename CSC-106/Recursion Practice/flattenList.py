def flatten_v2(alist):
    flattened_list = []
    for element in alist:
        if type(element) == type([]): 
            flattened_list = list(flattened_list) + flatten(element)
            
        else: 
            flattened_list.append(element) 

    return flattened_list
        







def flatten(alist):
    return flatten_v2(alist)




print(flatten_v2([[1,2,3],4,[6,[7,8]]]))