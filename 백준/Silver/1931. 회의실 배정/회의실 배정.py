N = int(input())

meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key = lambda x : (x[1], x[0]))

tmp = meeting[0][1]
cnt = 1

for meet in meeting[1:]:
    if meet[0] >= tmp:
        cnt += 1
        tmp = meet[1]

print(cnt)