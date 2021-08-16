S = input()

ans = 0

for b in range(2**(len(S)-1)):
    tmp = 0
    for i in range(len(S)):
        if (b>>i) & 1:
            ans += tmp*10 + int(S[i])
            tmp = 0
        else:
            tmp = tmp*10 + int(S[i])
    ans += tmp

print(ans)