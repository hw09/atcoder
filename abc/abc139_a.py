S = list(input())
T = list(input())

r = 0
for i, x in enumerate(S):
    if x == T[i]:
        r += 1
print(r)