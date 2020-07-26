# n = int(input())
# s = input()
# ans = s[:1]
# for i in range(1, n):
#     if ans[-1:] != s[i]:
#         ans += s[i]
# print(len(ans))

import itertools
n = int(input())
s = list(input())
ans = [k for k, v in itertools.groupby(s)]
print(len(ans))