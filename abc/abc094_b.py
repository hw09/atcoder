n, m, x = map(int, input().split())
a = [int(a) for a in input().split()]

large = []
small = []
for i in a:
    if x < i:
        large.append(i)
    else:
        small.append(i)

print(len(small) if len(small) < len(large) else len(large))
