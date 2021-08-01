X = []
for s in input():
    X.append(int(s))

ans = 'Strong'
if len(set(X)) == 1:
    ans = 'Weak'

flg = 0
for i in range(len(X)-1):
    if X[i] == 9 and X[i+1] == 0:
        flg += 1
    elif X[i+1] == X[i]+1:
        flg += 1
if flg == 3:
    ans = 'Weak'

print(ans)