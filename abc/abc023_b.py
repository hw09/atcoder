n = int(input())
s = input()

ans = 'b'

if n == 1:
    if ans == s:
        print(0)
        exit()
    else:
        print(-1)
        exit()

for i in range(1, 100+1):
    if i % 3 == 0:
        ans = 'b'+ans+'b'
    elif i % 3 == 1:
        ans = 'a'+ans+'c'
    elif i % 3 == 2:
        ans = 'c'+ans+'a'
    if s == ans:
        print(i)
        exit()
print(-1)
