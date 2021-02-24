import math

n = str(input())
if int(n) == 0:
    print('Yes')
    exit()

data_size = int (math.log10(int(n)) + 1)

ans = 0
for i in range(data_size):
    ans += int(n[i:i+1])

if ans % 9 == 0:
    print('Yes')
else:
    print('No')
