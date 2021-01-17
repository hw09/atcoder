s = input()
t = s[:len(s)//2]

for i in range(1, len(s)):
    s2 = s[:-i]
    t2 = s2[:len(s2)//2]
    if s2 == t2+t2:
        print(len(s2))
        break