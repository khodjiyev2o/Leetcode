from typing import List


def removeAnagrams(words: List[str]) -> List[str]:
    result = prev = []
    for i in range(len(words)):
        counter = [0] * 26
        for y in words[i]:
            counter[ord(y) - ord('a')] += 1
        if counter != prev:
            prev = counter
            result.append(words[i])
    return result

assert removeAnagrams(["abba","baba","bbaa","cd","cd"]) == ["abba","cd"]
assert removeAnagrams(["a","b","c","d","e"]) == ["a","b","c","d","e"]
assert removeAnagrams(["samandar","radnamas","msandara","qodir","qodiriy"]) == ['samandar','qodir', 'qodiriy']
assert removeAnagrams([]) == []


# Runtime 59 ms -- Beats 63.15%
# Memory 13.9 MB --  Beats 65.47%