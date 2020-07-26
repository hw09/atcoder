a, b, x = map(int, input().split())
n = 10**9
def price(n):
    return a * n + b * len(str(n))

if price(n) <= x:
    print(n)
    exit()

left = 0
right = 10**9
ans = 0
p = 0
while left <= right:
    mid = (left+right)//2
    p = price(mid)
    if p <= x:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1
print(ans)
    