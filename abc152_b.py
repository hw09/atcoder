a, b = map(int, input().split())

X = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(b):
    X[i] = str(a)
for j in range(a):
    Y[j] = str(b)

for k in range(9):
    if int(X[k]) < int(Y[k]):
        ｎX = [e for e in X if e != 0]
        print(''.join(nX))
        break
    elif int(X[k]) > int(Y[k]):
        ｎY = [e for e in Y if e != 0]
        print(''.join(nY))
        break
    else:
        if k == 8:
            ｎX = [e for e in X if e != 0]
            print(''.join(nX))
            