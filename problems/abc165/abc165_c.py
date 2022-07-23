from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
comb = list(combinations_with_replacement(range(1, m+1), n))
ans = [0] * len(comb)
for _ in range(q):
    a, b, c, d = map(int, input().split())
    for i in range(len(comb)):
        if comb[i][b-1] - comb[i][a-1] == c:
            ans[i] += d
print(max(ans))