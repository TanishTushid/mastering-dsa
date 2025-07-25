def merge_sort(arr):
    if len(arr) > 1 :
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        

        #recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        #merge sorted halves

        i = j = k = 0

        #compare and copy smaller element from left?/right into the origional array
        while i < len(left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

            #copy remaining elements of left_half
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print("origional arr: ",arr)
print("Sorted arr: ", merge_sort(arr))
