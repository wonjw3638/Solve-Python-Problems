# 1481_톱니바퀴
# 220916
'''
10:28 ~ 
'''
# 인덱스 헷갈리니까 앞에 리스트 하나 추가
Gear = [[0]] + [list(map(int, input())) for _ in range(4)]

K = int(input())

gear_idx ={
    'gear1' : 0,
    'gear2' : 0,
    'gear3' : 0,
    'gear4' : 0,
}

def rotate(gear, dire):
    rotated[gear] = 1

    # 오른쪽에 톱니바퀴가 있나 확인
    if (gear + 1) < 5:
        # idx+2 가 오른쪽 톱니랑 맞물리는 이, 오른쪽 톱니 기준 idx-2가 맞물리는 이
        # 만나는 이가 다른 경우 -> 다른 방향으로 회전
        if not rotated[gear+1]:
            if Gear[gear][((gear_idx['gear{}'.format(gear)])+2)%8] != Gear[gear+1][((gear_idx['gear{}'.format(gear+1)])-2)%8]:
                rotate(gear+1, -1 * dire)
            # 같은 경우 -> 멈춤
    # 왼쪽에 톱니바퀴가 있나 확인
    if (gear - 1) > 0:
        # 만나는 이가 다른 경우 -> 다른 방향으로 회전
        if not rotated[gear-1]:
            if Gear[gear][((gear_idx['gear{}'.format(gear)])-2)%8] != Gear[gear-1][((gear_idx['gear{}'.format(gear-1)])+2)%8]:
                rotate(gear-1, -1 * dire)

    # 회전시키기
    if dire == 1:
        gear_idx['gear{}'.format(gear)] -= 1
    else:
        gear_idx['gear{}'.format(gear)] += 1

    if (gear_idx['gear{}'.format(gear)] > 7) or (gear_idx['gear{}'.format(gear)] < -7):
        gear_idx['gear{}'.format(gear)] = gear_idx['gear{}'.format(gear)] % 8
    if gear_idx['gear{}'.format(gear)] < 0:
        gear_idx['gear{}'.format(gear)] = gear_idx['gear{}'.format(gear)] + 8


for k in range(K):
    # 1이 시계방향, -1이 반시계방향
    # idx -1, idx +1
    gear, dire = list(map(int, input().split()))
    # visited 함수 대용
    rotated = [0] * 5
    rotate(gear, dire)

# 점수계산 N : 0 S : 1
answer = 0

for idx in range(1, 5):
    if Gear[idx][gear_idx.get('gear{}'.format(idx))] == 1:
        answer += (2**(idx-1))

print(answer)