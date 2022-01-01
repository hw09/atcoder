n = int(input())
a = []
for i in range(2):
    a.append([int(x) for x in input().split()])

ans = 0
c = 0
for i in range(n):
    t1 = a[0][:i]
    t2 = a[1][i:]
    c = sum(t1) + sum(t2)
   
if ans < c:
    ans = c
print(ans)