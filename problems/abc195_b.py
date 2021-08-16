A, B, W = map(int, input().split())

W *= 1000

mi = W//B
ma = W//A

if W%B != 0:
    mi += 1

if mi > ma:
    print('UNSATISFIABLE')
else:
    print(mi, ma)