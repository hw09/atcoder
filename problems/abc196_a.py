a, b = map(int, input().split())
c, d = map(int, input().split())

print(max(a-c, a-d, b-c, b-d))