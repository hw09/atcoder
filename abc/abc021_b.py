n = int(input())
a, b = map(int, input().split())
k = int(input())
p = [int(x) for x in input().split()]

p.append(a)
p.append(b)

if len(set(p)) == len(p):
    print('YES')
else:
    print('NO')