N, M, X, Y = map(int, input().split())
x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
x.append(X)
y.append(Y)

if max(x) < min(y):
    print('No War')
else:
    print('War')