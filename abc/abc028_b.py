import collections
s = input()
S = collections.Counter(s)
ans = []
for k in ['A', 'B', 'C', 'D', 'E', 'F']:
    ans.append(str(S[k]))
print(' '.join(ans))