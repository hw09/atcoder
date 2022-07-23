n = int(input())
s = [list(input()) for _ in range(n)]

for i in range(n):
    for j in reversed(range(n)):
        print(s[j][i], end='')
    print()
