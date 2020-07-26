n, k = map(int, input().split())
a = [int(x) for x in input().split()]

ans = sum(a[0:k])
for i in range(1, n-k+1):
    nxt = ans - a[i-1] + a[i+k-1]
    if ans < nxt:
        print('Yes')
    else:
        print('No')
    ans = nxt
