N = int(input())
X = list(map(int, input().split())) 

cost = []

def mt(p):
    c = 0
    for i in range(len(X)):
        c += (X[i]-p)**2
    return c

for j in range(100):
    cost.append(mt(j))

print(min(cost))
