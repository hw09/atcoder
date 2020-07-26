n = int(input())
a = [int(x) for x in input().split()]

if sum(a) % n != 0:
    print(-1)
else:
    bridge = 0
    person = 0
    num = 0
    average = sum(a) // n

    for i in range(len(a)):
        person += a[i] - average
        num += 1
        if person == 0:
            bridge += num - 1
            person = 0
            num = 0
        
    print(bridge)
