from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
    result = []
    for i in nums:
        result.append(i**2)
    return sorted(result)


assert sortedSquares(nums = [-7,-3,2,3,11]) == [4,9,9,49,121]
assert sortedSquares(nums = [-4,-1,0,3,10]) == [0,1,9,16,100]
assert sortedSquares(nums = [-8,-2,2,3,11]) == [4,4,9,64,121]