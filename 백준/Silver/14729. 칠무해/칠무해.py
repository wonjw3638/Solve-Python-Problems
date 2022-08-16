# 14729_칠무해
import sys
input = sys.stdin.readline

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(float(input()))

for i in range(7):
    minIdx = i
    for j in range(i+1,N):
        if num_list[minIdx] > num_list[j]:
            minIdx = j
    num_list[minIdx], num_list[i] = num_list[i], num_list[minIdx]

for i in range(7):
    print('{:.3f}'.format(num_list[i]))