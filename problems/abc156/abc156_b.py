N, K = map(int, input().split())

def dec_to_n(X, n):
    if (int(X/n)):
        return dec_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

print(len(dec_to_n(N, K)))