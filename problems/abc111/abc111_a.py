n = input()

r = ''
for i in range(len(n)):
    r += '1' if n[i] == '9' else '9'

print(r)
