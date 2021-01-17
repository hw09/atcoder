n = int(input())
v = [int(v) for v in input().split()]
v.sort(reverse=True)
for i in range(1, n):
    vv = (v.pop() + v.pop())/2
    v.append(vv)
print(v[0])