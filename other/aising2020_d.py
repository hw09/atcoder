import copy
N = int(input())
x = list(input())

def popcount(s):
    return s.count('1')

memo = []
ans = []
for i in range(N):
    X = copy.deepcopy(x)
    X[i] = '1' if X[i]=='0' else '0'
    f = 0
    n = int(''.join(X), 2)
    while n != 0:
        n = n % popcount(bin(n))
        f += 1
    print(f)
