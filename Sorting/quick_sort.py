
def quick_sort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high) #get pivot index
        quick_sort(arr, low, pi - 1) #sort left side
        quick_sort(arr,pi+1,high)  #sort right side

def partition(arr,low,high):
    pivot = arr[high] #last element as pivot
    i = low - 1 # pointer for greater element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i] #swap
    
    arr[i+1],arr[high] = arr[high], arr[i+1] #swap pivot to correct position
    return i+1

arr = [10,7,8,9,1,5]
print("origional arr : ",arr)
quick_sort(arr, 0, len(arr)-1)
print("sorted array : ", arr)