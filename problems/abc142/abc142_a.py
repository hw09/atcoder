n = int(input())

even = [0]
odd = [0]
for i in range(n-1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(n if n == 1 else len(odd)/n)
