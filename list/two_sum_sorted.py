def twoSum(numbers: list[int], target: int) -> list[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            sumof = numbers[l] + numbers[r]
            if sumof == target:
                return [l + 1, r + 1]
            elif sumof > target:
                r -= 1
            elif sumof < target:
                l += 1 


assert twoSum(numbers = [2,3,4], target = 6) == [1, 3]
assert twoSum( numbers = [-1, 0], target = -1) == [1, 2]
assert twoSum(numbers = [2,7,11,15], target = 9) == [1,2]
