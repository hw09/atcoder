n, a, b = map(int, input().split())

q = n // (a + b)
m = n % (a + b)

if m <= a:
    print(q * a + m)
else:
    print(q * a + a)