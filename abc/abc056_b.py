W, a, b = map(int, input().split())
ans = 0
if a+W < b:
    ans = b - (a+W)
elif a > b+W:
    ans = a - (b+W)

print(ans)