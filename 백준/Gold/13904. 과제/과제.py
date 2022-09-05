import sys
input = sys.stdin.readline

N = int(input())
day = 0
hw_list = list()

for _ in range(N):
    hw = list(map(int, input().split()))
    if hw[0] > day:
        day = hw[0]
    hw_list.append(hw)

hw_list.sort(key = lambda x : x[1], reverse = True)

day_list = [0] * (day + 1)

for hw in hw_list:
    idx = hw[0]
    while idx > 0:
        if day_list[idx] == 0:
            day_list[idx] = hw[1]
            break
        else:
            idx -= 1

print(sum(day_list))