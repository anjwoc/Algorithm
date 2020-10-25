import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))
    que = [(idx, val) for idx, val in enumerate(que)]

    ans = 0
    while True:
        if que[0][1] == max(que, key=lambda x: x[1])[1]:
            ans += 1
            if que[0][0] == m:
                print(ans)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))
