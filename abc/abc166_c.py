n, m = map(int, input().split())
h = [int(x) for x in input().split()]
ans = [True] * n
for i in range(m):
    a, b = map(int, input().split())
    if h[a-1] < h[b-1]:
        ans[a-1] = False
    elif h[a-1] > h[b-1]:
        ans[b-1] = False
    else:
        ans[a-1] = False
        ans[b-1] = False
print(ans.count(True))
