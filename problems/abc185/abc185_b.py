N, M, T = map(int, input().split())
remaining = N
prev = 0
for _ in range(M):
    a, b = map(int, input().split())
    remaining -= a - prev
    if remaining <= 0:
        print('No')
        exit()
    remaining += b-a
    if remaining >= N:
        remaining = N
    prev = b

remaining -= T - prev
if remaining > 0:
    print('Yes')
else:
    print('No')