n = int(input())
a = [int(x) for x in input().split()]
ans = 0
for i in a:
    ans += 1 / i

print('{:.6f}'.format(1/ans))
