"""
Sum of given integers using  recursion  .
sum_recursive([1,3]) => 4
sum_recursive([4,5,2]) => 11
"""
def sum_recursive(nums: list[int]) -> int:
    if not nums:
        return 0
    return  sum_recursive(nums[:-1]) + nums.pop()

assert sum_recursive([1,3]) == 4
assert sum_recursive([4,5,2]) == 11
assert sum_recursive([9,9,9]) == 27
assert sum_recursive([-9, -9, -9]) == -27