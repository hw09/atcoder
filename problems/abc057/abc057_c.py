import math
n = int(input())
sqrtn = math.sqrt(n)
f = 0
ans = 10**10
for i in range(1, int(sqrtn)+1):
    div, mod = divmod(n, i)
    if mod == 0:
        f = max(len(str(div)), len(str(i)))
        if ans > f:
            ans = f
print(ans)