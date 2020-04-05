N, K, M = map(int, input().split())
A = list(map(int, input().split()))
fin = 0
for x in A:
    fin += x
X = M * N - fin
if 0 >= X:
    print(0)
elif X > K:
    print(-1)
else:
    print(X)
