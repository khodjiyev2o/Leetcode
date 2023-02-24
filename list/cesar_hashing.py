from typing import List

def encode(message: str) -> str:
    result = []
    for i in message:
        letter_order = ord(i) - ord('a') + 1
        new_letter = chr(ord('a') + letter_order + 2)
        result.append(new_letter)
    return "".join(result)
     
def decode(message: str) -> str:
    result = []
    for i in message:
        letter_order = ord(i) - ord('a') + 1
        new_letter = chr(ord('a') + letter_order - 4)
        result.append(new_letter)
    return "".join(result)

assert encode(message='abcdef') == 'defghi'
assert decode(message='defghi') == 'abcdef'

assert encode(message="Hello, World") == 'Khoor/#Zruog'
assert decode(message="Khoor/#Zruog") == 'Hello, World'
