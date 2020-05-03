S = input()

ans = 'AC'

if S[:1] != 'A':
    print('WA')
    exit()

if S[2:-1].count('C') != 1:
    print('WA')
    exit()

X = S[1:].split('C')
for x in X:
    if x.islower():
        pass
    else:
        print('WA')
        exit()

print(ans)