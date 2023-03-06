def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return s
        
assert reverseString(s = ["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert reverseString(s = ["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
assert reverseString(s = ["h","e","l","l","o"]) == ["o","l","l","e","h"]    
