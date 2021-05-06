N = int(input())
X = [int(x) for x in input().split()]

manhattan = 0
euclid = 0
chebyshev = 0

for x in X:
    manhattan += abs(x)
    euclid += abs(x) ** 2
    chebyshev = max(chebyshev, abs(x))

print(manhattan)
print(f'{euclid**0.5:.15f}')
print(chebyshev)
