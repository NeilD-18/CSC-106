alist = [2,5,4,1,3,10,9,7,6,8]
blist = [4,6,3,9,1]


def bubblesort(list): 

    max = len(list) - 1 

    for x in range(0,max):
        
        for y in range(0,max-x) :
            
            if list[y] > list[y+1]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp 

    print(list)

bubblesort(alist)
bubblesort(blist)