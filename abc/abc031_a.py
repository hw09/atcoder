a, d = map(int, input().split())
if a > d:
    d += 1
elif a <= d:
    a += 1
print(a*d)