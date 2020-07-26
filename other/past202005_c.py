a, r, n = map(int, input().split())
maxv = 10**9
maxva = maxv/a
ans = 1
if r == 1:
    print(a)
    exit()
for i in range(1, n+1):
    ans = r ** (i-1)
    if ans > maxva:
        print('large')
        exit()
print(ans*a)
