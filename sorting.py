
#swaps first and second values in an array
def python_swap(arr):
    arr[0],arr[1] = arr[1], arr[0]
    return arr

print(python_swap([1,2,3,4]))

#bookend swap python 
def bookend_swap_reverse(arr):
    start = 0
    end = len(arr)-1
    while(start<end):
        arr[start],arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    return arr

print(bookend_swap_reverse([1,2,3,4,5,6,7,8,9]))

#bubble sort
def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(0,len(arr)-1-j):
            if(arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1],arr[i]
    return arr

arr = [6,5,3,1,8,7,2,4]
bubble_sort(arr)

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

    # for i in range(len(arr)+1):
    #     for j in range(i,len(arr)-1):
    #         min = arr[j]
    #         if(arr[j]<min):
    #             min = arr[j]
    #     arr[i] = min
    # return arr

#insertion sort
# def insertion_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         min = arr[i]
#         print(arr)
#         for j in range(0, i+1):
#             print("Max index ",i)
#             print("Current index",j)
#             if(min>arr[j]):
#                 min = arr[j]
#                 min_index = j
#         arr.insert(i,arr.pop(min_index))
#         print(arr)
#         print("*"*50)
#     return arr
        
# arr = [6,5,3,1,8,7,2,4]
# insertion_sort(arr)

def insertion_sort1(arr):
    for i in range(len(arr)):
        min_index = i
        min = arr[i]
        for j in range(i,-1,-1):
            if(min>arr[j]):
                min_index = j
                min = arr[j]
        arr.pop(min_index)
        arr.insert(j,min)
    return arr
        
arr = [6,5,3,1,8,7,2,4]
insertion_sort1(arr)

def insertion_sort2(arr):
    for i in range(1,len(arr)):
        reference = arr[i]
        j = i-1
        while(j >= 0) and reference<arr[j]:
            arr[j+1] = arr[j]
            j-=1
            print(arr)
            arr[j+1] = reference
        print(arr)
    return arr

insertion_sort2(arr)
