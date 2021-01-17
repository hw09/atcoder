n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()
ans = 1
bus = t[0]+k
people = 0
for i in range(1, n):
    if t[i] < bus:
        if people <= c:
            people += 1
        else:
            ans +=1
            people = 1
    else:
        ans += 1
        people = 0
        bus = t[i]+k
print(ans)
