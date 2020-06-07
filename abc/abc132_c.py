n = int(input())
d = [int(x) for x in input().split()]
d.sort()
mid = n//2
print(d[mid]-d[mid-1])