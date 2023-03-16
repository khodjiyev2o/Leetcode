def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    
    while n > 1:
        if n%2 == 1:
            return False
        n//=2
    return  True

def is_power_of_two2(n: int) -> bool:
    if n <= 0:
        return False
    while n%2 == 0:
        n //= 2
    return True if n == 1 else False 


def tests():
    try:
        assert is_power_of_two(n=16) == True
        print("First test passed successfully")
    except Exception:
        print(f"First test failed !{Exception}")
    try:
        assert is_power_of_two(n=0) == False
        print("Second test passed successfully")
    except Exception:
        print(f"Second test failed !{Exception}")
    try:
        assert is_power_of_two(n=1) == True
        print("Second test passed successfully")
    except Exception as e:
        print(f"Second test failed !{e}")

def tests2():
    try:
        assert is_power_of_two2(n=16) == True
        print("First test for second version passed successfully")
    except Exception:
        print(f"First test for second version failed !{Exception}")
    try:
        assert is_power_of_two2(n=0) == False
        print("Second test for second version passed successfully")
    except Exception:
        print(f"Second test for second version failed !{Exception}")
    try:
        assert is_power_of_two2(n=1) == True
        print("Second test for second version passed successfully")
    except Exception as e:
        print(f"Second test for second version failed !{e}")


tests()
tests2()