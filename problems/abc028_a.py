n = int(input())
ans = 'Perfect'
if n <= 59:
    ans = 'Bad'
elif n <= 89:
    ans = 'Good'
elif n <= 99:
    ans = 'Great'
print(ans)