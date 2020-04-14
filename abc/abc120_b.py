A, B, K = map(int, input().split())
C = 0
for i in range(min(A, B),  0, -1):
    if A%i == 0 and B%i == 0:
        C += 1
        if C == K:
            break
print(i)
