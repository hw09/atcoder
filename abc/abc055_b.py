n = int(input())
INF = 10**9+7

ans = 1
for i in range(1, n+1):
    ans = (i * ans)%INF 
print(ans)