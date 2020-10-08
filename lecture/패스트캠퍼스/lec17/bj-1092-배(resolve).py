import sys

n = int(input())
cranes = list(map(int, input().split()))

m = int(input())
boxes = list(map(int, input().split()))

# 모든 박스를 옮길 수 없는 경우
if max(cranes) < max(boxes):
    print(-1)
    sys.exit()

positions = [0] * n
visited = [False] * m
cranes.sort(reverse=True)
boxes.sort(reverse=True)

ans = 0
cnt = 0

while True:
    if cnt == len(boxes):
        break
    for i in range(n):
        while positions[i] < len(boxes):
            if not visited[positions[i]] and cranes[i] >= boxes[positions[i]]:
                visited[positions[i]] = True
                positions[i] += 1
                cnt += 1
                break
            positions[i] += 1
    ans += 1
print(ans)
