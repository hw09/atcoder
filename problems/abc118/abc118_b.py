N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for y in range(N)]
ans = set(int(z) for z in range(1, 31))
for i in range(N):
    A[i].pop(0)
    ans = ans & set(A[i])
print(len(ans))
