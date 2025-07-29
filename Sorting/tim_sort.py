# Helper function to use Insertion Sort on a run
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Helper function to merge two sorted halves
def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Get minimum run size
def get_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r

# TimSort main function
def tim_sort(arr):
    n = len(arr)
    minrun = get_minrun(n)

    # Step 1: Sort individual runs using insertion sort
    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(arr, start, end)

    # Step 2: Merge runs
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size

# Example usage
arr = [5, 21, 7, 23, 19]
print("Before Sort:", arr)
tim_sort(arr)
print("After Sort:", arr)
