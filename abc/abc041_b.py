a, b, c = map(int, input().split())
MAX = 10**9+7

print(((a%MAX)*(b%MAX)*(c%MAX))%MAX)