a, b, c = map(int, input().split())

x, y = divmod(c, min(a, b))
z = y//max(a, b)
print(x+z)