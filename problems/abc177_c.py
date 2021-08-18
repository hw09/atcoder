N = int(input())
A = list(map(int, input().split()))

MOD = 10**9+7
ans = 0
SUM = A[0]

for i in range(1, N):
    ans += SUM * A[i]
    SUM += A[i]
    
print(ans%MOD)
