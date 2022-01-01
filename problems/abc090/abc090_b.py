a, b = map(int, input().split())

def palindrome(string): return True if string==string[::-1] else False
ans = 0
for i in range(a, b+1):
    if palindrome(str(i)):
        ans += 1
print(ans)