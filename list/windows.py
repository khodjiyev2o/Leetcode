# Given the array of integers and k - integer. Return the maximum of numbers between the each given interval 
# Testcase 1 :
# arr=[6, 2, 3, 7], k=3
# output: arr= [6, 7]

def solution(arr: list[int], k: int) -> list[int]:
    if len(arr) < k:
        return []
    right = k 
    left = 0 
    result = []
    while right <= len(arr):
        result.append(max(arr[left:right]))
        left += 1 
        right += 1
    return result

assert solution(arr=[6, 2, 3, 7], k=3) == [6, 7]
assert solution(arr=[6, 2, 3, 7, 0, 1], k=3) == [6, 7, 7, 7]
assert solution(arr=[3, 3, 3], k=3) == [3]