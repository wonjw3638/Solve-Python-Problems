N = int(input())
liquids =  list(map(int, input().split()))
liquids.sort()
answer = [0, 0]
tmp = 2000000001

start = 0
end = N-1

while start < end:
    if liquids[start] + liquids[end] < 0:
        if tmp > abs(liquids[start] + liquids[end]):
            answer[0] = liquids[start]
            answer[1] = liquids[end]
            tmp = abs(liquids[start] + liquids[end])
        start += 1

    elif liquids[start] + liquids[end] > 0:
        if tmp > abs(liquids[start] + liquids[end]):
            answer[0] = liquids[start]
            answer[1] = liquids[end]
            tmp = abs(liquids[start] + liquids[end])
        end -= 1

    else:
        answer[0] = liquids[start]
        answer[1] = liquids[end]
        break

print(*answer)