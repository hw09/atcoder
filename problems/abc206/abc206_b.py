N = int(input())

for i in range(1, 10**9+1):
    if (i**2+i)/2 >= N:
        break
print(i)
