s = list(input())
t = int(input())

pos = [0, 0]
p = 0
for i in s:
    if i == 'L':
        pos[0] -= 1
    elif i == 'R':
        pos[0] += 1
    elif i == 'U':
        pos[1] += 1
    elif i == 'D':
        pos[1] -= 1
    elif i == '?':
        p += 1
    
man = abs(pos[0]) + abs(pos[1])

if t == 1:
    man += p
elif t == 2:
    man = max(len(s)%2, man-p)

print(man)
