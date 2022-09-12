N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_1 = cnt0 = cnt1 = 0

def cut(i, j, N):
    global cnt_1, cnt0, cnt1
    if N == 1:
        if paper[i][j] == -1: cnt_1 += 1
        elif paper[i][j] == 0: cnt0 += 1
        else: cnt1 += 1
        return 
    
    else:
        tmp = paper[i][j]
        chk = False

        for di in range(N):
            for dj in range(N):
                if paper[i + di][j + dj] == tmp:
                    continue
                else:
                    chk = True
                    break
        
        if chk == False:
            if tmp == -1: cnt_1 += 1
            elif tmp == 0: cnt0 += 1
            else: cnt1 += 1
            return
        else:
            cut(i, j, N//3)
            cut(i + N//3, j, N//3)
            cut(i + (2 * (N//3)), j, N//3)
            cut(i, j + N//3, N//3)
            cut(i + N//3, j + N//3, N//3)
            cut(i + (2 * (N//3)), j + N//3, N//3)
            cut(i, j + (2 * (N//3)), N//3)
            cut(i + N//3, j + (2 * (N//3)), N//3)
            cut(i + (2 * (N//3)), j + (2 * (N//3)), N//3)
        return 

cut(0, 0, N)
print(cnt_1)
print(cnt0)
print(cnt1)