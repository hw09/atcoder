N = int(input())
name = []
for _ in range(N):
    name.append(input())

if len(set(name)) == N:
    print('No')
else:
    print('Yes')