n, q = map(int, input().split())
arr = [0 for _ in range(n)]
for _ in range(q):
    l, r, t = map(int, input().split())
    for i in range(l-1, r):
        arr[i] = t
for j in arr:
    print(j)