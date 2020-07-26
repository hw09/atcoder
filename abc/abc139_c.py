n = int(input())
h = [int(x) for x in input().split()]

ans = 0
cur = 1
cnt = 0
while cur < n:
    if h[cur-1] >= h[cur]:
        cnt += 1
        cur += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
        cur += 1
ans = max(ans, cnt)
print(ans)
