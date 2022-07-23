from collections import Counter

N = int(input())
S = []
for _ in range(N):
    S.append(input())

mycounter = Counter(S).most_common()[::1]
result = []
maxcount = mycounter[0][1]
for i in range(len(mycounter)):
    if maxcount == mycounter[i][1]:
        result.append(mycounter[i][0])

result.sort()
for j in range(len(result)):
    print(result[j])
