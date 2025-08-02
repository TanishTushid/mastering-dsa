
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 # search right side
        else:
            high = mid - 1 # search left side
    
    return -1  #target not found

arr = [2,4,6,8,10,12,14,16]
target = 10

result = binary_search(arr,target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
