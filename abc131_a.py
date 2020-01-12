S = list(input())

for i, x in enumerate(S):
    if i == len(S)-1:
        print('Good')
        break
    elif S[i] == S[i+1]:
        print('Bad')
        break
    else:
        pass