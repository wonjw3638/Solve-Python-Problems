S = list(input())
T = list(input())

lenT = len(T)
lenS = len(S)

answer = 0

while lenT >= lenS:
    if T == S:
        answer = 1
        break
    else:
        if T[-1] == 'A':
            T.pop()
            lenT -= 1
        else:
            T.pop()
            T = T[::-1]
            lenT -= 1

print(answer)