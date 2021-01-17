N = int(input())
n = [int(x) for x in list(str(N))]
if N % sum(n) == 0:
    print('Yes')
else:
    print('No')
