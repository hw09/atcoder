N, A, X, Y = map(int, input().split())

if N > A:
    ans = X * A + Y * (N - A)
else:
    ans = X * N
print(ans)