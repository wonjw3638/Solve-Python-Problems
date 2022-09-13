for tc in range(1, 11):
    N = int(input())
    arr = [[0,0,0] for _ in range(N+1)]

    # 트리 정보 저장
    for idx in range(1, N+1):
        info = list(input().split())
        idx = int(info[0])
        if len(info) == 4:
            arr[idx][0] = info[1]
            arr[idx][1] = int(info[2])
            arr[idx][2] = int(info[3])
        elif len(info) == 3:
            arr[idx][0] = info[1]
            arr[idx][1] = int(info[2])
        else:
            arr[idx][0] = info[1]
    
    answer = ''

    # 중위순회 탐색 함수 구현
    def inorder_traverse(node):
        global answer
        if arr[node][1]:
            inorder_traverse(arr[node][1])
        answer += arr[node][0]
        if arr[node][2]:
            inorder_traverse(arr[node][2])

    inorder_traverse(1)

    print('#{} {}'.format(tc, answer))