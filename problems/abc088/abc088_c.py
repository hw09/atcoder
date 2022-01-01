# 二重三重のループは値を固定してループの段数を少なくする
c = []
for _ in range(3):
    c.append([int(x) for x in input().split()])

a = [0]
b = [c[0][i] for i in range(3)]

for j in range(1, 3):
    a.append(c[j][j] - b[j])
ans = 'Yes'
for k in range(3):
    for m in range(3):
        if c[k][m] != a[k] + b[m]:
            ans = 'No'
            break
print(ans)