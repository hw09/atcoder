n = int(input())
a = [int(input())-1 for _ in range(n)]
ans = 1
place = a[0]
for i in range(n):
    if place == 1:
        break
    else:
        place = a[place]
        ans += 1
if place == 1:
    print(ans)
else:
    print(-1)
