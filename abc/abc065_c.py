import math
n, m = map(int, input().split())

N = math.factorial(n)
M = math.factorial(m)
INF = 10**9 + 7

if abs(n-m) > 1:
    print(0)
elif abs(n-m) == 1:
    print(N*M%INF)
else:
    print(2*N*M%INF)