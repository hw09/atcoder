N = int(input())
T, A = map(int, input().split())
H = [int(x) for x in input().split()]
ans = 0
near_a = 1000000
for i in range(N):
    temp = T - H[i] *0.006
    if near_a > abs(A - temp):
        near_a = abs(A - temp)
        ans = i + 1
print(ans)