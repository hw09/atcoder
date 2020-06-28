import itertools
s = input()
k = int(input())

ans = []
for i in range(len(s)-k+1):
    tmp = s[i:i+k]
    if tmp not in ans:
        ans.append(tmp)

print(len(ans))
