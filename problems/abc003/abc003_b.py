s = input()
t = input()
a = ['a', 't', 'c', 'o', 'd', 'e', 'r']
ans = True
for i in range(len(s)):
    if s[i] == t[i]:
        pass
    else:
        if s[i] == '@':
            if t[i] == '@' or t[i] in a:
                pass
            else:
                ans = False
                break
        elif t[i] == '@':
            if s[i] == '@' or s[i] in a:
                pass
            else:
                ans = False
                break
        else:
            ans = False
            break

print('You can win' if ans else 'You will lose')