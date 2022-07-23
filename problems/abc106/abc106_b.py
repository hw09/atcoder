N = int(input())

ans = 0

def mkdivisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

for i in range(1, N+1):
    if i % 2 != 0:
        if len(mkdivisors(i))==8:
            ans += 1
print(ans)