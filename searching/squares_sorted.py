from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    result = []
    for i in nums:
        result.append(i**2)
    return sorted(result)


assert sortedSquares(nums = [-7,-3,2,3,11]) == [4,9,9,49,121]
assert sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]
assert sortedSquares(nums = [-8,-2,2,3,11]) == [4,4,9,64,121]


def sortedSquares2(nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l]**2 > nums[r]**2 :
                result.append(nums[l] ** 2)
                l += 1 
            elif nums[l]**2 < nums[r]**2:
                result.append(nums[r] ** 2)
                r -= 1 
            else:
                result.append(nums[l] ** 2)
                l += 1
        return result[::-1]


assert sortedSquares2(nums = [-7,-3,2,3,11]) == [4,9,9,49,121]
assert sortedSquares2(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]
assert sortedSquares2(nums = [-8,-2,2,3,11]) == [4,4,9,64,121]

# The second solution is better than the first one in terms of time complexity
# because it has a linear time complexity of O(n), 
# whereas the first solution has a time complexity of O(nlogn) due to the sorting step.

# Additionally, the second solution does not require any additional space beyond the output list,
# whereas the first solution creates a new list result, which can be considered additional space.

