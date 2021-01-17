import itertools

n = int(input())
p = [int(x)-1 for x in input().split()]
q = [int(x)-1 for x in input().split()]

L = list(itertools.permutations(range(n)))

P = L.index(tuple(p))
Q = L.index(tuple(q))
print(abs(P-Q))
