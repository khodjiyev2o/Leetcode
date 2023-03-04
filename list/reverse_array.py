def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

assert rotate_array(nums = [1,2,3,4,5,6,7], k = 3) == [5,6,7,1,2,3,4]

nums = [1,2,3,4,5]
print(5%3)
nums.reverse()
print(nums)
nums[:2] = reversed(nums[:2])
nums[2:] = reversed(nums[2:])
print(nums)