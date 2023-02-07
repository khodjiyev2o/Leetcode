"""
valid_brackets("()()") = True
valid_brackets("{()[]}") = True
valid_brackets("{(]}") = False
"""
def valid_brackets(s: str) -> bool:
    stack = []
    brackets = {
        '}' :  '{',
        ']' : '[',
        ')' : '(' 
    }
    for char in s:
        if not char in brackets:
            stack.append(char)
            continue
        if brackets[char] in stack:
            stack.pop()
            continue
        return False
    return True if not stack  else False

assert valid_brackets("()()") == True
assert valid_brackets("{()[]}") == True
assert valid_brackets("{(]}") == False
assert valid_brackets("(){[][]") == False
