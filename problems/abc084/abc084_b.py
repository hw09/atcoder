a, b = map(int, input().split())
s = input()
if s.count('-') == 1:
    s1, s2 = s.split('-')
    print('Yes' if a == len(s1) and b == len(s2) else 'No')
else:
    print('No')