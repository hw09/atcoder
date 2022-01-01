N = int(input())
A = list(map(int, input().split()))

tmp = sorted(A)
print(A.index(tmp[-2])+1)
