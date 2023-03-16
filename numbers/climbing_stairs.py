def climbStairs(n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
             two, one = one, one + two 

        return one


assert climbStairs(n=4) == 5
assert climbStairs(n=3) == 3
assert climbStairs(n=2) == 2