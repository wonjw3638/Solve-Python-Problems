import sys

G = int(input())
P = int(input())

airPlane = [int(sys.stdin.readline()) for _ in range(P)]
Gate = [i for i in range(G + 1)]

# 부모노드 찾기
def find(x):
    if x == Gate[x]:
        return x
    else:
        # 부모노드로 루트 변경하기
        Gate[x] = find(Gate[x])
        return Gate[x]

answer = 0

for plane in airPlane:
    find_plane = find(plane)
    if not find(plane):
        # 찾았는데 0 나오면
        break
    else:
        # 비행기 도킹
        answer += 1
        # Gatep[find_plane] 에 비행기 찼으니까 그 옆에 Gate로 부모노드 변경
        Gate[find_plane] = Gate[find_plane - 1]

print(answer)