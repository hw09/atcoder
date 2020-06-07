n, k, q = map(int, input().split())

a = [0]*n
for _ in range(q):
    a[int(input())-1] += 1

for i in range(n):
    point = k - q + a[i]
    if point > 0:
        print('Yes')
    else:
        print('No')
