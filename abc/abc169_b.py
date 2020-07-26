n = int(input())
a = [int(x) for x in input().split()]

maxval = 10 ** 18
ans = 1


for i in range(n):
    ans *= a[i]
    if ans > maxval:
        ans = -1
        break
    
if 0 in a:
    ans = 0
    
print(ans)