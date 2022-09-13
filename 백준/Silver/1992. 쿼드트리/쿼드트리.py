N = int(input())
paper = [list(input()) for _ in range(N)]

def cut(i, j, N):
    if N == 1:
        if paper[i][j] == '0': return '0' 
        else: return '1'
    
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
            if tmp == '0': return '0'
            else: return '1'
            
        else:
            return f'({cut(i, j, N//2)}{cut(i, j + N//2, N//2)}{cut(i + N//2, j, N//2)}{cut(i + N//2, j + N//2, N//2)})'
         
answer = cut(0, 0, N)
print(answer)