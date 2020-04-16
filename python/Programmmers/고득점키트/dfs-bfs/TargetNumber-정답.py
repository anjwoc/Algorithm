ans = 0


def dfs(idx, numbers, target, value):
    global ans
    n = len(numbers)
    if idx == n and target == value:
        ans += 1
        return
    if idx == n:
        return

    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])


def solution(numbers=[1, 1, 1, 1, 1], target=3):
    global ans

    dfs(0, numbers, target, 0)
    return ans


print(solution())
