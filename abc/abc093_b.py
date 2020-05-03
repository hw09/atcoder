a, b, k = map(int, input().split())
for i in range(a, a+k):
    if a <= i <= b:
        print(i)

for j in range(b-k+1, b+1):
    if i < j <= b:
        print(j)