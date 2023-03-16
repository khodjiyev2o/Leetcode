def pivotIndex(nums: list[int]) -> int:
        leftSum, rightSum = 0, 0
        for i in range(len(nums)):
            if i == 0:
                leftSum = 0
                rightSum = sum(nums[i+1:]) 
            elif i == len(nums) - 1:
                rightSum = 0
                leftSum = sum(nums[:i])
            else:
                leftSum = sum(nums[:i])
                rightSum = sum(nums[i+1:]) 
            if leftSum == rightSum:
                    return i
        return -1

def pivotIndex2(nums: list[int])-> int:
    leftSum, rightSum = 0, sum(nums)
    for i in range(len(nums)):
        if leftSum == rightSum - leftSum - nums[i]:
            return i
        leftSum += nums[i]
    return -1

assert pivotIndex(nums=[1,7,3,6,5,6]) == 3
assert pivotIndex2(nums=[1,7,3,6,5,6]) == 3