n = int(input())
a = list(set([int(input()) for _ in range(n)]))
a.sort(reverse=True)
print(a[1])
