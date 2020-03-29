X = int(input())

ans = 0
coin = [500, 5, 1]

for i in coin:
    r, X = divmod(X, i)
    if i == 500:
        ans += r * 1000
    elif i == 5:
        ans += r * 5
    else:
        pass
print(ans)
