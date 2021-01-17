N, M = map(int, input().split())
a = [int(x) for x in input().split()]
if N >= sum(a):
    print(N-sum(a))
else:
    print('-1')