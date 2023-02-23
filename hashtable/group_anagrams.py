from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    count = 0
    result = []
    newDict = {}
    for word in strs:
        counter = [0] * 26
        for y in word:
            counter[ord(y) - ord('a')] += 1
        for key, value in newDict.items():
            to_add = 1
            if value == counter:
                result[key].append(word)
                to_add = 0
                break
        if not newDict or to_add:
            newDict[count] = counter
            result.append([word])
            count += 1      
    return result

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    result = {}
    for word in strs:
        chars = ''.join(sorted(word))
        if chars in result:
            result[chars].append(word)
        else:
            result[chars] = [word]
    return [x for x in result.values()]

assert groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert groupAnagrams(strs = [""]) == [[""]]
assert groupAnagrams(strs = ["a"]) == [["a"]]
assert groupAnagrams(strs=["samandar","samandar","radnamas","qodir","ridoq","ravnaq"]) == [['samandar', 'samandar', 'radnamas'], ['qodir', 'ridoq'], ['ravnaq']]


assert groupAnagrams2(strs=["samandar","samandar","radnamas","qodir","ridoq","ravnaq"]) == [['samandar', 'samandar', 'radnamas'], ['qodir', 'ridoq'], ['ravnaq']]
assert groupAnagrams2(strs=["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
assert groupAnagrams2(strs = [""]) == [[""]]
assert groupAnagrams2(strs = ["a"]) == [["a"]]