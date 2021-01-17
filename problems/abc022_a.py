n, s, t = map(int, input().split())
ans = 0
w = int(input())
if s <= w <= t:
    ans += 1
for i in range(n-1):
    w += int(input())
    if s <= w <= t:
        ans += 1
print(ans)