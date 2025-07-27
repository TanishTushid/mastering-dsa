
def counting_sort(arr):
    if not arr:
        return arr
    max_value = max(arr)
    count = [0]*(max_value+1)

    #count each element
    for num in arr:
        count[num] += 1 
    
    #accumulate the counts
    for i in range(1,len(count)):
        count[i] += count[i - 1]
    
    #build the output array
    output = [0]*len(arr)
    for num in reversed(arr): #reverse for stable sort
        count[num] -= 1
        output[count[num]] = num
    return output

arr = [4,2,2,8,3,3,1]
print("origional array: ",arr)
counting = counting_sort(arr)
print("Sorted array: ", counting)