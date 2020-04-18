S = input()
ans = []
for i in range(len(S)-2):
    ans.append(abs(753 - int(S[i:i+3])))
print(min(ans))