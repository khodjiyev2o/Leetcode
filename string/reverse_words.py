def reverseWords(s: str) -> str:
        result = []
        words = s.split()
        for word in words:
            word = "".join(reversed(word))
            result.append(word)
        return " ".join(result)

assert reverseWords(s = "Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverseWords(s = "God Ding") == "doG gniD"
