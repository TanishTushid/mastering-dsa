class InfiniteArray:
    def __init__(self, data):
        self.data = data

    def get(self, index):
        # Simulate infinite array by returning 'inf' for out-of-bound indexes
        if index < len(self.data):
            return self.data[index]
        return float('inf')


def infinite_binary_search(arr_obj, target):
    # Step 1: Define search window
    start = 0
    end = 1

    # Expand window until target is less than or equal to arr[end]
    while arr_obj.get(end) < target:
        start = end
        end *= 2

    # Step 2: Perform binary search in the defined window
    while start <= end:
        mid = start + (end - start) // 2
        value = arr_obj.get(mid)

        if value == target:
            return mid
        elif value < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # target not found


# Example usage:
if __name__ == "__main__":
    data = [2, 4, 6, 10, 13, 18, 22, 25, 30, 34, 50, 60, 75, 80, 100, 120, 150]
    arr_obj = InfiniteArray(data)

    target = 100
    result = infinite_binary_search(arr_obj, target)

    if result != -1:
        print(f"Target {target} found at index: {result}")
    else:
        print(f"Target {target} not found in array.")
