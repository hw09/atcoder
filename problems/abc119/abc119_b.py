ans = 0
for _ in range(int(input())):
    x, u = input().split()
    if u == 'JPY':
        ans += int(x)
    else:
        ans += float(x) * 380000.0
print(ans)