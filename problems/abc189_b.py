N, X = map(int, input().split())

d = 0
for i in range(N):
    V, P = map(int, input().split())
    d += V * P

    if X*100 < d:
        print(i+1)
        exit()
print(-1)
