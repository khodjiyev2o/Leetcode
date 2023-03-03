import random
def search(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
        


nums = [-1,0,3,5,9,12]
assert search(nums=nums, target=5) == 3
assert search(nums=nums, target=9) == 4
assert search(nums=nums, target=0) == 1
assert search(nums=nums, target=12) == 5


def isBadVersion(num: int) -> bool:
    if num <= 0:
        return False
    arr = [False, False, False, True, True]
    return arr[num - 1]

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

assert firstBadVersion(n=5) == 4
assert firstBadVersion(n=4) == 4
assert firstBadVersion(n=6) == 4


