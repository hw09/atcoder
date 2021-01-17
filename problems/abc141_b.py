S = list(input())
odd = S[0::2]
even = S[1::2]
if ('R' not in even) and ('L' not in odd):
    print('Yes')
else:
    print('No')
