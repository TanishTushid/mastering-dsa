
def counting_sort(arr,exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10 # for digits 0-9

    #count occurrences of digits at exp place
    for i in range(n):
        index = (arr[i]//exp)%10
        count[index] += 1

    #accumulate counts
    for i in range(1,10):
        count[i] += count[i - 1]

    #build output (stable sort)
    i = n-1
    while i >= 0:
        index = (arr[i] // exp)%10
        output[count[index] -1] = arr[i]
        count[index] -= 1
        i -= 1

    #copy back to origional array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return 
    #find max number to get number of digits
    max_num = max(arr)

    #sort by each digit 
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10



arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)



