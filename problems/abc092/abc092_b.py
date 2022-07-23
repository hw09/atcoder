n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

eat = 0
for i in range(n):
    one = 1
    while one <= d:
        one += a[i]
        eat += 1
print(x + eat) 
