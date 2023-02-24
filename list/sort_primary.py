# Testcase #1
# [1, 2, 3]
# [1, 4, 9]

# Testcase #2
# [-5, 1, 2, 3]
# [-25, 1, 4, 9]

def solution(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        if numbers[i] < 0:
            result.append(-numbers[i] ** 2)
        else:
            result.append(numbers[i] ** 2)
    return result

assert solution(numbers=[-5, 1, 2, 3]) == [-25, 1, 4, 9]
assert solution(numbers=[1, 2, 3]) == [1, 4, 9]
assert solution(numbers=[0, 1, 2, 3]) == [0, 1, 4, 9]