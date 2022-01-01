n = int(input())
a = input().split()
a_odd = a[1::2]
a_even = a[0::2]

if n % 2 == 0:
    a_odd.reverse()
    ans = a_odd + a_even
else:
    a_even.reverse()
    ans = a_even + a_odd
print(' '.join(ans))