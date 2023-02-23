"""
Testing:
is_anagram("lama", "alam") => True
is_anagram("mosh", "shom") => True
is_anagram("non", "nok") => False
"""

def is_anagram(word1: str, word2: str) -> bool:
    newDict = {}
    for i in word1:
        if i in newDict:
            newDict[i] += 1
        else:
            newDict[i] = 1
    for k in word2:
        if k in newDict and newDict[k] != 0:
            newDict[k] -= 1
        else:
            return False
    return True

def isAnagram(word1: str, word2: str) -> bool:
        newDict = {}
        for i in word1:
            if i in newDict:
                newDict[i] += 1
            else:
                newDict[i] = 1
        for i in word2:
            if i not in newDict or newDict[i] <= 0:
                return False
        return True

assert is_anagram("lama", "alam") == True
assert is_anagram("mosh", "shom") == True
assert is_anagram("non", "nok") == False


assert isAnagram("lama", "alam") == True
assert isAnagram("mosh", "shom") == True
assert isAnagram("non", "nok") == False