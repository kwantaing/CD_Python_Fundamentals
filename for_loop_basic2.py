def biggie_size(list):
    for i in range(len(list)):
        if(list[i]>0):
            list[i] = "big"
    return list
print(biggie_size([-1,3,5,-5]))

def count_positives(list):
    count = 0
    for vals in list:
        if(vals > 0 ):
            count+=1
    list[len(list)-1] = count
    return list
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(list):
    sum = 0
    for vals in list:
        sum+=vals
    return sum
print(sum_total([1,2,3,4]))

def avg(list):
    sum = 0
    for vals in list:
        sum+=vals
    avg = sum/len(list)
    return avg
print(avg([1,2,3,4]))

def length(list):
    return len(list)

print(length([1,4,2,2]))

def mini(list):
    if(len(list)==0):
        return False
    min = list[0]
    for val in list:
        if(val<min):
            min = val
    return min
mini([37,2,1,-9])

def max(list):
    if(len(list)==0):
        return False
    max = list[0]
    for val in list:
        if(val>max):
            max = val
    return max
max([37,2,1,-9])

def ult_analysis(list):
    sumTotal = 0
    min = list[0]
    max = list[0]
    for val in list:
        sumTotal+=val
        if(val>max):
            max = val
        if(val<min):
            min = val
    return{
        'sumTotal': sumTotal,
        'average':sumTotal/len(list),
        'minimum':min,
        'maximum':max,
        'length': len(list)
    }
print(ult_analysis([37,2,1,-9]))

def reverse_list(list):
    start = 0
    end = len(list)-1
    while(start<end):
        temp = list[start]
        list[start] = list[end]
        list[end] = temp
        start+=1
        end-=1
    return list
print(reverse_list([37,2,1,-9]))