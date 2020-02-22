N = int(input())
A = list(map(int, input().split()))

def has_duplicates(seq):
    return len(seq) != len(set(seq))

print('NO' if has_duplicates(A) else 'YES')