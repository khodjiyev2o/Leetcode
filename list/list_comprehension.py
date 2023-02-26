def solution(arr: list[int]) -> list[int]:
    return [x for x in arr for x in x]

def solution(x):
    b = []
    for x in x:
        for x in x:
            b.append(x)
    return b

print(solution([[1,2,3],[4,5,6]]))
