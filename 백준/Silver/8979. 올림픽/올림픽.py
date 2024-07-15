N, K = map(int, input().split())

countries = [[-1, -1, -1] for i in range(N+1) ]

for _ in range(N):
    i, g, s, b = map(int, input().split())
    if i == K:
        target_score = [g, s, b]
    countries[i] = [g, s, b]

cnt = 1

for score in countries:
    if score[0] > target_score[0]: cnt += 1
    elif score[0] == target_score[0]:
        if score[1] > target_score[1]: cnt += 1
        elif score[1] == target_score[1]:
            if score[2] > target_score[2]: cnt +=1

print(cnt)