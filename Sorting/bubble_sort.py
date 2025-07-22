

# basic bubble sort (no early exit)

def bubble_sort(arr):
    n= len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# optimized bubble sort (with early exit)

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False # track if any swaps happen
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                #swap if elements in wrong order
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break # exit early if already sorted
    return arr

if __name__=="__main__":
    arr = list(map(int,input("enter numbers separated by space: ").split()))

    print("original array:")
    print(arr)
    #use optimmized bubble sort
    sorted_arr = bubble_sort_optimized(arr.copy())

    print("\nsorted array (optimized bubble sort):")
    print(sorted_arr)

    # for reference, also show basic bubble sort result
    sorted_basic = bubble_sort(arr.copy())
    print("\nsorted array (basic bubble sort):")
    print(sorted_basic)