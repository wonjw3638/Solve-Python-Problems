import sys
input = sys.stdin.readline

N, H = list(map(int, input().split()))
obstacle1 = [0] * H
obstacle2 = [0] * H

for n in range(N):
    h = int(input())
    if n % 2:
        obstacle1[0] += 1
        obstacle1[h] -= 1

    else:
        obstacle2[0] += 1
        obstacle2[h] -= 1

for idx in range(1, H):
    obstacle1[idx] = obstacle1[idx] + obstacle1[idx-1]
    obstacle2[idx] = obstacle2[idx] + obstacle2[idx-1]

obstacle = [0] * H
obstacle2 = obstacle2[::-1]
tmp = N + 1
cnt = 0
for i in range(H):
    obstacle[i] = obstacle1[i] + obstacle2[i]
    if obstacle[i] < tmp:
        tmp = obstacle[i]
        cnt = 1
    elif obstacle[i] == tmp:
        cnt += 1
    else:
        continue
        
print(tmp, cnt)