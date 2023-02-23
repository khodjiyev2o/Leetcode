def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    newDict = {}
    result = []
    for p, h in zip(names, heights):
        newDict[h] = p
    heights.sort()
    for i in heights[::-1]:
        if i in newDict:
            result.append(newDict[i])
    return result


assert sortPeople(names=["Mary","John","Emma"], heights=[180,165,170]) == ["Mary","Emma","John"]
assert sortPeople(names=["Alice","Bob","Bob"], heights=[155,185,150]) == ["Bob","Alice","Bob"]
