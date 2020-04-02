N = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
c = [int(z) for z in input().split()]

total = 0
pre = 999
for i in range(N):
    total += b[a[i]-1]
    if a[i] == pre+1:
        total += c[pre-1]
    pre = a[i]
print(total)