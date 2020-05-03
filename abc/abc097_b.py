X = int(input())
ans = 1
for b in range(1,X):
    for p in range(2, X):
        if X < b**p:
            break
        if ans < b**p:
            ans = b**p
print(ans)