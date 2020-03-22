S = input()
def is_batch(s):
    return True if s==s[::-1] else False

ans = 'No'
n = len(S)
if is_batch(S):
    if is_batch(S[0:(n//2)]):
        if is_batch(S[(n+2)//2:n+1]):
            ans = 'Yes'
print(ans)
