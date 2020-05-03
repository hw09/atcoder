# a = int(input())
# b, c = map(int, input().split())
# s = input()

# print('{} {}'.format(a+b+c, s))

# a, b = map(int, input().split())
# print('Even' if a*b % 2 == 0 else 'Odd')

# s = input()
# print(s.count('1'))

# n = int(input())
# a = [int(x) for x in input().split()]

# ans = 0
# flg = True
# while flg:
#     for i in range(n):
#         div, mod = divmod(a[i], 2)
#         if mod == 0:
#             a[i] = div
#         else:
#             flg = False
#     ans += 1
# print(ans-1)    

# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
# ans = 0
# for i in range(a+1):
#     for j in range(b+1):
#         for k in range(c+1):
#             if 500*i + 100*j + 50*k == x:
#                 ans += 1
# print(ans)

# n, a, b = map(int, input().split())
# ans = 0
# for i in range(1, n+1):
#     if a <= sum(map(int, str(i))) <= b:
#         ans += i
# print(ans)

# n = int(input())
# a = [int(x) for x in input().split()]

# a.sort(reverse=True)
# alice = a[::2]
# bob = a[1::2]
# print(sum(alice)-sum(bob))

# n = int(input())
# d = [int(input()) for _ in range(n)]
# print(len(set(d)))

n = int(input())
