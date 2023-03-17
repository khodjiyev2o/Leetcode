def isSubsequence(s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        i, y = 0, 0
        while y < len(t):
            if s[i] == t[y]:
                i += 1
                y +=1
            else:
                y += 1
            if i == len(s):
                return True
        return False