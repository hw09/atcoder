n, k = map(int, input().split())

ans = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(b):
        ans.append(a)
ans.sort()
print(ans[k-1])