n = int(input())
a = [int(x) for x in input().split()]
ans = 0
flg = True
while flg:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            flg = False
            break
    if flg:
        ans += 1
print(ans)