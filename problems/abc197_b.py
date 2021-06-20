H, W, X, Y = map(int, input().split())

gred = []
for _ in range(H):
    gred.append(input())

ans = 0

for i in reversed(range(X)):
    if gred[i][Y-1] == '.':
        ans += 1
    else:
        break

for j in range(X-1, H):
    if gred[j][Y-1] == '.':
        ans += 1
    else:
        break

for k in range(Y-1, W):
    if gred[X-1][k] == '.':
        ans += 1
    else:
        break

for l in reversed(range(Y)):
    if gred[X-1][l] == '.':
        ans += 1
    else:
        break

print(ans-3)
