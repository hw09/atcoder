a = [int(input())]
i = 0

def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

while True:
    A = f(a[i])
    if A in a:
        break
    else:
        a.append(A)
        i += 1
            
print(i+2)