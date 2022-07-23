n = int(input())
print('Yes' if n % sum(list(map(int, str(n)))) == 0 else 'No')