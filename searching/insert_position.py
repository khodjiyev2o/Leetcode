def searchInsert(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

assert searchInsert(nums = [1,3,5,6], target = 5) == 2
assert searchInsert(nums = [1,3,5,6], target = 2) == 1
assert searchInsert(nums = [1,3,5,6], target = 7) == 4

def searchInsert2(nums: list, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    return i

assert searchInsert2(nums = [1,3,5,6], target = 5) == 2
assert searchInsert2(nums = [1,3,5,6], target = 2) == 1
assert searchInsert2(nums = [1,3,5,6], target = 7) == 4