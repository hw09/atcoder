N, L = map(int, input().split())

R = L + N - 1

eat = 0
if R <= 0:
    eat = R
elif L >= 0:
    eat = L
else:
    eat = 0

ans = (R + L) * (R - L + 1) // 2 - eat
print(ans)