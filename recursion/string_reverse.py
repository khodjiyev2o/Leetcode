"""
Return reversed string using recursion
For example :
reverse_recursive("space") => "ecaps"
reverse_recursive("where") => "erehw"
"""

def reverse_recursive(word: str) -> str:
    if len(word) == 1:
        return word[0]
    return word[-1] + reverse_recursive(word[:-1])

assert reverse_recursive(word='space') == "ecaps"
assert reverse_recursive(word='where') == "erehw"
assert reverse_recursive(word='Samandar') == "radnamaS"