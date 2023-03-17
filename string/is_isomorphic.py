def isIsomorphic1(s: str, t: str) -> bool:
    zipped_set = set(zip(s, t))
    return len(zipped_set) == len(set(s)) == len(set(t))

def isIsomorphic2(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        newDict = {}
        for i in range(len(s)):
            if s[i] in newDict:
                s = s[:i] + newDict[s[i]] + s[i+1:]
            else:
                if t[i] in newDict.values():
                    return False
                newDict[s[i]] = t[i]
                s = s[:i] + t[i] + s[i+1:]
        return True if s == t else False


def tests():
    try:
        assert isIsomorphic1(s = "egg", t = "add") == True
        print("Test # 1 passed")
    except:
         print("Test # 1 failed")
    try:
        assert isIsomorphic1(s = "foo", t = "bar") == False
        print("Test # 2 passed")
    except:
         print("Test # 2 failed")
    try:
        assert isIsomorphic1(s = "paper", t = "title") == True
        print("Test # 3 passed")
    except:
         print("Test # 3 failed")
    print("Running 2 set of tests")
    try:
        assert isIsomorphic2(s = "egg", t = "add") == True
        print("Test # 1 passed")
    except:
         print("Test # 1 failed")
    try:
        assert isIsomorphic2(s = "foo", t = "bar") == False
        print("Test # 2 passed")
    except:
         print("Test # 2 failed")
    try:
        assert isIsomorphic2(s = "paper", t = "title") == True
        print("Test # 3 passed")
    except:
         print("Test # 3 failed")
tests()