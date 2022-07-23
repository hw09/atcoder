s = input()
n = int(input())

def ss(s):
    l, r = map(int, input().split())
    ls = s[:l-1]
    ms = s[l-1:r][::-1]
    rs = s[r:]
    return ls+ms+rs

for i in range(n):
    s = ss(s)

print(s)