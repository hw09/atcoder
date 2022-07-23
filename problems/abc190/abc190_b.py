N, S, D = map(int, input().split())
for _ in range(N):
    X, Y = map(int, input().split())
    if S > X and D < Y:
        print('Yes')
        exit()
print('No')