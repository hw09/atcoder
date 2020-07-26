import copy
n = int(input())
a = [int(input()) for _ in range(n)]

b = copy.deepcopy(a)
b.sort()
max1 = b[-1]
max2 = b[-2]

for i in a:
    if i == max1:
        print(max2)
    else:
        print(max1)
