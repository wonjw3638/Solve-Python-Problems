N = int(input())
liquids =  list(map(int, input().split()))
liquids.sort()
tmp = 200000001

start = 0
end = N-1

while start < end:
    if liquids[start] + liquids[end] < 0:
        if abs(tmp) > abs(liquids[start] + liquids[end]):
            tmp = liquids[start] + liquids[end]
        start += 1

    elif liquids[start] + liquids[end] > 0:
        if abs(tmp) > abs(liquids[start] + liquids[end]):
            tmp = liquids[start] + liquids[end]
        end -= 1

    else:
        tmp = 0
        break

print(tmp)