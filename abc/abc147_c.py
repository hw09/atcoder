import itertools

n = int(input())
persons = list(itertools.product([0, 1], repeat=n))
testimony = [[] for _ in range(n)]


for i in range(n):
    num = int(input())
    for j in range(num):
        person, state = map(int, input().split())
        testimony[i].append([person-1, state])

honest = 0
for i in range(1, 2**n):
    flag = 0
    for j in range(n):
        if (i>>j)&1 == 1:
            for x, y in testimony[j]:
                if (i>>x)&1 != y:
                    flag = 1
                    break
    if flag == 0:
        honest = max(honest, bin(i)[1:].count('1'))
print(honest)
