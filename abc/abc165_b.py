import math
x = int(input())
a = 100
ans = 0
while True:
    a += math.floor(a * 0.01)
    ans += 1
    if a >= x:
        print(ans)
        exit()