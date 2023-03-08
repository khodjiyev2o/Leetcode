def lengthOfLongestSubstring(s: str) -> int:
        elements = {}
        max_substring, start = 0, 0
        for i in range(len(s)):
            if s[i] in elements and elements[s[i]] >= start:
                start = elements[s[i]] + 1
            else:
                max_substring = max(max_substring, i + 1 - start)
            elements[s[i]] = i
        return max_substring


assert lengthOfLongestSubstring(s = "abcabcbb") == 3
assert lengthOfLongestSubstring(s = "bbbbb") == 1   
assert lengthOfLongestSubstring(s = "pwwkew") == 3
assert lengthOfLongestSubstring(s = "dvdf") == 3
