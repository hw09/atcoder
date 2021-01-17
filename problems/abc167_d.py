n, k = map(int, input().split())
a = [int(x) for x in input().split()]
A = [False] * n
t = ''
nxt = a[0]

for i in range(k):
    nxt = a[nxt]-1
    A[nxt] = True
    t = t + str(a[nxt])
    if A[nxt] == True:
        break
print(t[-1:])
