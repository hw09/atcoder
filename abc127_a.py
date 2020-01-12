A, B = map(int, input().split())
if A >= 13:
    plice = B
elif A >= 6:
    plice = B/2
else:
    plice = 0
print(int(plice))
