A, B = map(int, input().split())

result = 'No'
for i in range(3):
    if (A * B * i) % 2 == 1:
        result = 'Yes'
print(result)
