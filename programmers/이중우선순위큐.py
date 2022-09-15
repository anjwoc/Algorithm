import heapq as hq


def solution(ops):
    que = []

    for op in ops:
        char, num = op.split()
        num = int(num)
        if char == 'I':
            hq.heappush(que, num)
        elif char == 'D' and num == 1:
            if len(que) > 0:
                que.pop()
        elif char == 'D' and num == -1:
            if len(que) > 0:
                hq.heappop(que)

    if len(que) == 0:
        return [0, 0]
    else:
        lst = sorted(que)
        return [lst[-1], lst[0]]
