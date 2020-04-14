import math
N, D = map(int, input().split())
X = []
for _ in range(N):
    X.append([int(x) for x in input().split()])

count = 0
for i in range(N):
    for j in range(i+1, N):
        dist = 0
        for k in range(D):
            dist += abs(X[i][k] - X[j][k]) ** 2

        if math.sqrt(dist).is_integer():
            count += 1
        
print(count)