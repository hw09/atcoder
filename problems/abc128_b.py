# 多重キーでソート

# A = [['ABC', 1, 3], ['ZBC', 3, 2], ['DEF', 1, 4]]
# print(sorted(A, key=lambda x: (x[1], -x[2])))

N = int(input())
X = [[input().split(), i + 1] for i in range(N)]
X = sorted(X, key=lambda x: (x[0][0], -int(x[0][1])))
for i in range(N):
    print(X[i][1])