
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i #current index in minimum
        #find the index of the minimum element in the rest of the array
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j

        #swap if new minimum is found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print("origional array -> ",arr)
print("sorted array array -> ",selection_sort(arr))
