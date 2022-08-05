import sys
N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))
max = max(list)

for i in range(N):
    list[i] = list[i]/max*100

avr = sum(list)/N
print(avr)
