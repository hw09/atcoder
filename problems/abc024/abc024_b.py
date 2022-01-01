n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.reverse()
ans = t
for i in range(n-1):
    if a[i] - a[i+1] < t:
        ans += a[i] - a[i+1]
    else:
      ans += t

print(ans)
