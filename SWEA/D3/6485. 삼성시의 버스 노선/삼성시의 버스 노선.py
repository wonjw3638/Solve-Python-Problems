T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    routes = []
    for _ in range(N):
        routes.append(list(map(int, input().split())))
    
    P = int(input())

    answer = '#{}'.format(tc)
    for _ in range(P):
        C = int(input())
        bus = 0
        for route in routes:
            if ( route[0] <= C ) and ( route[1] >= C ):
                bus += 1
        answer += (' ' + (str(bus)))
    
    print(answer)