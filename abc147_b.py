S = list(input())
ans = 0
for i, s in enumerate(range(len(S)//2)):
    if S[i] == S[-(i+1)]:
        pass
    else:
        S[-(i+1)] = S[i]
        ans += 1
print(ans)
