n = int(input())
ans = 0
for i in range(n+1):
    if i**2 <= n:
        ans = i**2
    else:
        break
print(ans)