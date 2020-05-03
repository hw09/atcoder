n = int(input())
L = [2, 1]
for i in range(2, n+1):
    L.append(L[i-1] + L[i-2])
print(L[n])