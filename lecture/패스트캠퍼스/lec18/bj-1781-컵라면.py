import sys

input = sys.stdin.readline
n = int(input())
arr = dict()
for _ in range(n):
    a, b = map(int, input().split())
    if a not in arr:
        arr[a] = [b]
    else:
        arr[a] += [b]

items = sorted(arr.items(), key=lambda x: x[0])

ans = 0
dead = 0
visited = set()
for i in range(len(items)):
    idx = i + 1
    deadline, noodle = items[i]
    if deadline >= n:
        break

    if deadline == idx:
        ans += max(noodle)
    else:
        for i in noodle:
            if deadline <= i:
                ans += i
            deadline += 1


print(ans)