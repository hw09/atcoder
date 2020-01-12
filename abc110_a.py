A, B, C = map(int, input().split())
L = [A, B, C]
L.sort()

print(L[2]*10+L[1]+L[0])