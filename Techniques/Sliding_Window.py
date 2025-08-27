
# Fixed Size Window 

def max_subarray_sum(nums, k):
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k , n):
        window_sum += nums[i] - nums[i-k]  #slide window
        max_sum = max(max_sum, window_sum)
    return max_sum

#Variable size window 
def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:   # shrink window
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    b = 5
    print(max_subarray_sum(a,b))

    print(min_subarray_len(7, [2,3,1,2,4,3]))
