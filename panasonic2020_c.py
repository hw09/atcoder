import numpy as np
a, b, c = map(int, input().split())

if np.sqrt(a)+np.sqrt(b) < np.sqrt(c):
    print('Yes')
else:
    print('No')