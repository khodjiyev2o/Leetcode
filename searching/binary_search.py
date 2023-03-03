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

