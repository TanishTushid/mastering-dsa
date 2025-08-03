

def binary_search_2d(matrix, target):
    if not matrix or not matrix[0]:
        return False # empty matrix
    
    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        #convert 1D index to 2D index
        row = mid // cols
        col = mid % cols
        mid_val = matrix[row][col]

        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1,3,5],[7,9,11],[13,15,17]]
target = 9 
print(binary_search_2d(matrix,target))