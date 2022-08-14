T = int(input())

def my_max(a_list):
    answer = a_list[0]
    for a in a_list:
        if a > answer:
            answer = a
    return answer

for tc in range(1, T+1):
    N = int(input())
    # 1~1000 인데 index 헷갈리니까 1001개 생성
    bus_stop = [0] * 1001  

    for _ in range(N):
        bus, start, end = list(map(int, input().split()))

        # 일반버스 일 때 
        if bus == 1: 
            for stop in range(start, end + 1):
                bus_stop[stop] += 1
        # 급행버스 일 때 
        elif bus == 2: 
            num = start%2
            for stop in range(start, end):
                # 홀/짝 결과가 같을 때만 방문
                if (stop % 2) == num:   
                    bus_stop[stop] += 1
            # 도착지점 따로 추가
            bus_stop[end] += 1   
        # 광역 급행일 때
        else: 
            # 홀수 일 때
            if start%2: 
                for stop in range(start, end):
                    if ((stop%3) == 0 and (stop%10) != 0):
                        bus_stop[stop] += 1
                bus_stop[end] += 1
            # 짝수 일 때
            else: 
                for stop in range(start, end):
                    if (stop%4) == 0:
                        bus_stop[stop] += 1
                bus_stop[end] += 1

    print('#{} {}'.format(tc, my_max(bus_stop)))