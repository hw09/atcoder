N = int(input())
S = [input() for _ in range(N)]
ans = 'Yes'
for i in range(1, N):
    if S[i-1][-1:] != S[i][:1]:
        ans = 'No'
        break
if len(S) != len(set(S)):
    ans = 'No'
print(ans)