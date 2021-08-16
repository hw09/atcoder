N, X = map(int, input().split())
A = list(map(int, input().split()))

p = 0
for i in range(N):
    if (i+1) % 2 == 0:
        p += A[i]-1
    else:
        p += A[i]

print('Yes' if X >= p else 'No')
