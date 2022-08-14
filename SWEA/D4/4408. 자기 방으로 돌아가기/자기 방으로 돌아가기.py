T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [0] * 401
    for _ in range(N):
        source, dest = list(map(int, input().split()))
        if source < dest:
            # 도착지점이 홀수라면 그 다음 짝수까지 +1
            if dest % 2: 
                for i in range(source, dest + 2):
                    rooms[i] += 1
            else: 
                for i in range(source, dest + 1):
                    rooms[i] += 1
        else:
            # 도착지점이 짝수라면 그 전 홀수까지 +1
            if dest % 2:
                for i in range(dest, source - 1):
                    rooms[i] += 1
            else:
                for i in range(dest - 1, source - 1):
                    rooms[i] += 1
    
    answer = 0
    for m in rooms:
        if m > answer:
            answer = m

    print('#{} {}'.format(tc, answer))