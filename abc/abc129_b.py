N = int(input())
W = [int(x) for x in input().split()]

S1 = 0
S2 = 0
ans = 999
for i in range(N):
    s = abs(sum(W[0:i+1]) - sum(W[i+1:]))
    if ans > s:
        ans = s
print(ans)