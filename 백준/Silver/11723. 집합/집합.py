import sys
input = sys.stdin.readline

# 연산의 수 M
M = int(input())

# 공집합 S
S = [False] * 21

for _ in range(M):
    msg = input().strip()
    if msg == 'all':
        S = [True] * 21
    elif msg =='empty':
        S = [False] * 21
    else:
        msg, n = msg.split()
        n = int(n)
        if msg == 'add':
            if S[n] == False:
                S[n] = True
        if msg == 'remove':
            if S[n] == True:
                S[n] = False
        if msg == 'check':
            if S[n] == True:
                print(1)
            else:
                print(0)
        if msg == 'toggle':
            if S[n] == True:
                S[n] = False
            else:
                S[n] = True