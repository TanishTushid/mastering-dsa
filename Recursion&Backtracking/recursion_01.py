class calculate_factorial:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        return self._factorial_recursive(self.n)
    
    def _factorial_recursive(self,num):
        if num == 0:
            return 1
        else:
            return num * self._factorial_recursive(num - 1)

p= calculate_factorial(5)
print(f"factorial {p.factorial()}")


def sum_of_n_nums(nums):
    if nums == 1:
        return 1
    else:
        return nums + sum_of_n_nums(nums-1)
 
p = sum_of_n_nums(5)
print(f"sum of nums {p}")


def fibonacci(nums):
    if nums == 0 or nums == 1:
        return nums
    else:
        return fibonacci(nums - 1) + fibonacci(nums - 2)
    
p = fibonacci(3)
print(f"fibonacci : {p}")

def is_sorted(nums):
    if len(nums) <= 1:
        return True
    if nums[-1] <nums[-2]:
        return False
    return is_sorted(nums[:-1])
    
nums = [1, 2, 3, 4, 5]
print(f"is sorted: {is_sorted(nums)}")
