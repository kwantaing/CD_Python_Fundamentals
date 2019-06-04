#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        min = arr[i]
        for j in range(i,len(arr)):
            if min>arr[j]:
                min = arr[j]
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
        print(arr)
    return arr


arr=[8,5,2,6,9,3,1,4,0,7] 
selection_sort(arr)