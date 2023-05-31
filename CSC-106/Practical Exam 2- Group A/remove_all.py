#Neil Daterao

#Program that creates a new list that removes a target number from the given list

def remove_all(list, target):

    #Create a new list, in which we'll add the numbers that aren't the target 
    new_list = []

    #Iterate through all numbers in the list 
    for num in list:

        #If the number doesn't equal the target, add it to the list
        if num != target:
            new_list.append(num)

    return new_list


### DO NOT DELETE THIS LINE: beg testing

target = 3
list = []
print("Removing", target, "from", list, "yields", remove_all(list, target))

list = [2,4,6,3,2,1,3,3]
print("Removing", target, "from", list, "yields", remove_all(list, target))

target = 2
list = [2,4,2,2,5,6,4]
print("Removing", target, "from", list, "yields", remove_all(list, target))

