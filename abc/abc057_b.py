n, m = map(int, input().split())
student = []
for _ in range(n):
    student.append([int(x) for x in input().split()])
chkpoint = []
for _ in range(m):
    chkpoint.append([int(x) for x in input().split()])

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for i in range(n):
    minx = 10**9
    goto = 0
    for j in range(m):
        tmp = dist(student[i], chkpoint[j])
        if minx > tmp:
            minx = tmp
            goto = j+1
    print(goto)
    