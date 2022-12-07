import sys, heapq
input = sys.stdin.readline

# 테스트 케이스 정수 T
T = int(input())
for _ in range(T):
    # 적용할 연산의 개수 k
    k = int(input())
    # 연산을 저장할 최소힙MinQ, 최대힙MaxQ
    MinQ = list()
    MaxQ = list()
    
    # 제거한 것 체크할 리스트
    removed = [False] * k

    # k번 연산을 반복
    for k_idx in range(k):
        msg, n = input().split()
        # 연산이 'I'인 경우
        if msg == 'I':
            heapq.heappush(MinQ, (int(n), k_idx))
            heapq.heappush(MaxQ, (-int(n), k_idx))
        # 연산이 'D'인 경우
        else:
            # 최댓값을 삭제하는 연산
            if n == '1':
                while MaxQ:
                    # MaxQ에서 가장 작은 값 => 최댓값
                    maxNum, idx = heapq.heappop(MaxQ)
                    if removed[idx] == False:
                        removed[idx] = True
                        break
                    else: continue                                          
            # 최솟값을 삭제하는 연산
            else:
                while MinQ:
                    # MinQ에서 가장 작은 값 => 최솟값
                    minNum, idx = heapq.heappop(MinQ)
                    if removed[idx] == False:
                        removed[idx] = True
                        break
                    else: continue                                          

    maxNum, minNum = None, None

    while MaxQ:
        maxNum, idx = heapq.heappop(MaxQ)
        if removed[idx] == False:
            break
        else: 
            maxNum = None
            continue
                           
    while MinQ:
        minNum, idx = heapq.heappop(MinQ)
        if removed[idx] == False:
            break
        else: 
            minNum = None
            continue

    if maxNum and minNum :
        print(-maxNum, minNum)
    else:
        print('EMPTY')