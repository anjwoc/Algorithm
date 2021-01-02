from collections import deque


def solution(people, limit):
    boat = 0
    que = deque(sorted(people))

    while que:
        # 2명 이상일 때
        if len(que) >= 2:
            if que[0] + que[-1] <= limit:
                que.pop()
                que.popleft()
                boat += 1
            elif que[0] + que[-1] > limit:
                que.pop()
                boat += 1
        else:
            # 1명
            if que[0] <= limit:
                que.pop()
                boat += 1
    return boat


print(solution([70, 50, 80, 50], 100))
