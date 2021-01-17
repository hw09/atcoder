n = int(input())
a = [int(x) for x in input().split()]

ans = 0

for i in range(n):
    if a[i] == 8 or a[i] == 4 or a[i] == 2:
        ans += 1
    elif a[i] == 5:
        ans += 2
    elif a[i] == 6:
        ans += 3
print(ans)
