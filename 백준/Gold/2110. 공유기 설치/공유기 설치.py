def can_place_routers(houses, distance, routers_count):
    count = 1  # 첫 번째 집에는 공유기를 무조건 설치
    last_installed = houses[0]

    for i in range(1, len(houses)):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]
            if count >= routers_count:
                return True
    return False

def find_max_min_distance(houses, routers_count):
    houses.sort()

    left = 1
    right = houses[-1] - houses[0]
    best_distance = 0

    while left <= right:
        mid = (left + right) // 2
        if can_place_routers(houses, mid, routers_count):
            best_distance = mid
            left = mid + 1
        else:
            right = mid - 1

    return best_distance

# 입력 예시
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# 최대 최소 거리 찾기
result = find_max_min_distance(houses, C)
print(result)
