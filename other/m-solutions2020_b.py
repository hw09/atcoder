a, b, c = map(int, input().split())
k = int(input())

for i in range(k):
    if c <= b:
        c *= 2
    elif b <= a:
        b *= 2

if c > b and b > a:
    print('Yes')
else:
    print('No')