import math
n = int(input())
x = int(math.sqrt(n))
if n == 1:
    print(0)
    exit()
ans = []
for i in range(x, 0, -1):
    for j in range(x, n):
        m = n - (i * j)
        if m < 0:
            break
        s = abs(i-j)
        ans.append(m+s)
ans.sort()
print(ans[0])
                