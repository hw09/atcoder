S = input()

SO = ''
SE = ''

for i in range(0, len(S), 2):
    SO += S[i]

for j in range(1, len(S), 2):
    SE += S[j]

if str(SO).islower():
    if str(SE).isupper() or str(SE) == '':
        print('Yes')
        exit()
print('No')