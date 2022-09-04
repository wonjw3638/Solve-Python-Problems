A, B = list(map(int, input().split()))
answer = -1
cnt = 1
while A <= B:
    if A == B:
        answer = cnt
        break
    if B % 10 == 1:
        B = B // 10
        cnt += 1
    elif B % 2 == 0:
        B = B // 2
        cnt += 1
    else:
        break

print(answer)