a, b, c, x, y = map(int, input().split())
ans = 5000 * (10**5) * 2 + 1
for i in range(max(x, y)+1):
    A = a * (x - i) if x-i > 0 else 0
    B = b * (y - i) if y-i > 0 else 0
    C = 2 * c * i
    v = A + B + C
    if ans > v:
        ans = v
print(ans)
