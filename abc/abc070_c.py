import functools
import fractions
n = int(input())
t = [int(input()) for _ in range(n)]

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)
    
ans = functools.reduce(lcm, t)
print(ans)