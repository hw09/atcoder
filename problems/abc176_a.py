n, x, t = map(int, input().split())

count = n // x if n % x == 0 else n // x + 1
print(count * t)
