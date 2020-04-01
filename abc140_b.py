N = int(input())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
c = [int(z) for z in input().split()]

total = 0
pre = 0
for i in a:
    total += b[i-1]
    if i-1 == pre:
        total += c[pre]
    pre = i
print(total)