def countdown(number):
    newlist = []
    for i in range(number,-1,-1):
        newlist.append(i)
    return newlist

# print(countdown(5))

def print_return(list):
    print(list[0])
    return(list[1])

# print(print_return([1,2]))

def first_plus_length(list):
    return list[0]+len(list)

# print(first_plus_length([1,2,3,4,5]))

def vals_greater_than_second(list):
    newlist = []
    count=0
    for i in list:
        if(i>list[1]):
            newlist.append(i)
            count+=1
    print(count)
    if (len(newlist)<2):
        return False
    return newlist

# print(vals_greater_than_second([5,2,3,2,1,4]))

def this_l_that_val(size,value):
    newlist=[]
    for i in range(size):
        newlist.append(value)
    return newlist

# print(this_l_that_val(4,7))
