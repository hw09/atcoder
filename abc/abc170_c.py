x, n = map(int, input().split())
if n == 0:
    print(x)
    exit()

p = [int(x) for x in input().split()]
ans = 10**9

if x not in p:
    ans = x
else:
    for i in range(1, 101):
        minus = x-i
        plus = x+i
        if minus not in p:
            ans = minus
            break
        elif plus not in p:
            ans = plus
            break
print(ans)