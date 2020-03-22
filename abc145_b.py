N = int(input())
S = input()

c = len(S)//2
fs = S[c:]
ls = S[:c]

if fs == ls:
    print('Yes')
else:
    print('No')