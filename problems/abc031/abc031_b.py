l, h = map(int, input().split())
n = int(input())
for _ in range(n):
    a = int(input())
    ans = 0
    if l > a:
        ans = l - a
    elif h < a:
        ans = -1
    print(ans)
