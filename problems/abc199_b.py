N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(1001):
    if max(A) <= i <= min(B):
        ans += 1
print(ans)