import math
x = int(input())

def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = math.sqrt(n)

    data = [i+1 for i in range(2, n, 2)]
    while limit > data[0]:
        prime.append(data[0])
        data = [j for j in data if j % data[0] != 0]
    return prime + data

plist = get_prime(200000)
ans = 0
for y in range(x, 200000):
    if y in plist:
        ans = y
        break
    else:
        pass

print(ans)