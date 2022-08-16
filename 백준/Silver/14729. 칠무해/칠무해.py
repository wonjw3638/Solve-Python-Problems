# 14729_칠무해
import sys
input = sys.stdin.readline

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(float(input()))

num_list.sort()
for i in range(7):
    print('{:.3f}'.format(num_list[i]))