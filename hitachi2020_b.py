A, B, M = map(int, input().split())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

x = [0] * M
y = [0] * M
c = [0] * M

ans = 10 ** 10
for i in range(M):
    x[i], y[i], c[i] = map(int, input().split())
    p = a[x[i]-1] + b[y[i]-1] - c[i]
    if ans > p:
        ans = p
    
if ans > min(a) + min(b):
    ans = min(a) + min(b)

print(ans)