
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  #current element
        j = i - 1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]  #shift element right
            j -= 1
            arr[j + 1] = key
    return arr

arr = [5, 2, 4, 6, 1, 3]
print("sorted : ",insertion_sort(arr))