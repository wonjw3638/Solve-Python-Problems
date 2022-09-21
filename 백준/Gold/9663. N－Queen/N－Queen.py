# 9663 N-Queen
# 220920

N = int(input())
answer = 0

chess = [[0] * N for _ in range(N)]

# i번째줄에 queen을 놓을 수 있는 자리 확인
def queen(i, chess):
    global answer

    # 마지막 줄 까지 다 한 경우
    if i == N:
        answer += 1
        return 

    if chess[i] == [1] * N:
        return

    for j in range(N):
        # i, j에 queen 놓을 수 있으면 놓고 밑에 줄들에 queen 놓을 수 없는 자리 표시 후 다음줄 탐색
        if chess[i][j] == 0:
            # 원본 바뀌니까 딥카피, 전달
            chessIQueen = [chess[i][:] for i in range(N)]
            # 같은 행 - 확인 필요x
            # 같은 열
            for r in range(i+1, N):
                chessIQueen[r][j] = 1
            # 대각선 아래
            for k in range(1,N-i):
                # 왼쪽아래
                if 0 <= j-k < N:
                    chessIQueen[i+k][j-k] = 1
                # 오른쪽아래
                if 0 <= j+k < N:
                    chessIQueen[i+k][j+k] = 1
            # 다음 줄 확인        
            queen(i+1, chessIQueen)

queen(0, chess)
print(answer)