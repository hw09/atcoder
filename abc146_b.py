import string
N = int(input())
S = list(input())

al = list(string.ascii_uppercase)
ans = []
for i in S:
    pos = al.index(i) + N
    if pos < 26:
        ans.append(al[pos])
    else:
        ans.append(al[pos-26])
print(''.join(ans))
