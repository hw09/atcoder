s = list(input())
n = int(input())

y = []
for i in s:
    for j in s:
        y.append(i+j)
y.sort()
print(y[n-1])
