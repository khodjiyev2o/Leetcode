"""
For example :
two_sum([1,4,5,2], 3) => True # as 1 + 2 are present in the list, 1 + 2 = 3
two_sum([1,4,5,2], 8) => False
"""
def two_sum(arr: list[int], target: int) -> bool:
    complements = {}
    for i in arr:
        subsc = target - i
        if subsc in complements:
            return True
        else:
            complements[i] = subsc
    return False

assert two_sum([1, 4, 5, 2], 3) == True
assert two_sum([1,4,5,2], 8) == False
assert two_sum([11, 41, 7, 9], 18) == True