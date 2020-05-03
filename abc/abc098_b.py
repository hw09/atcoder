import string
N = int(input())
S = list(input())

ans = 0
for i in range(1, N):
    left = S[:i]
    right = S[i:]
    common = set(left) & set(right)
    if ans < len(common):
        ans = len(common)

print(ans)