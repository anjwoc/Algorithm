import copy
from collections import defaultdict

"""
주어진 항공권을 모두 써서 여행경로를 짠다.
항상 ICN에서 출발
방문하는 항공 경로를 담아서 return한다.
tickets[a][b] 는 a에서 b로가는 항공권이다.
만약에 가능 경로가 2개면 알파벳 순서가 앞서는 경로로 return
방문 불가능한 경우는 없다.
"""


def dfs(start, path, arr, ans, n):
    # 이동 경로 저장
    arr.append(start)
    for i in range(len(path[start])):
        # 이미 방문했으면 건너 뛴다.
        if path[start][i] == True:
            continue
        else:
            # 해당 경로에서 도착할 수 있는 다음 경로 탐색
            next_path = path[start][i]
            # 다음 경로의 visited여부를 True로 반환
            path[start][i] = True

            # 다음 경로에서 진행 가능한 경로 탐색
            tmp = dfs(next_path, path, arr, ans, n)
            # 주어진 항공권을 모두 사용해 경로를 만들 수 있는 경우
            if len(tmp) == n + 1:
                ans.append(copy.deepcopy(tmp))
            # 백트래킹
            arr.pop()
            # 백트래킹 해야하니 경로를 다시 돌려놓는다.
            path[start][i] = next_path

    return arr


def solution(tickets):
    ans = []
    path = defaultdict(list)

    for ticket in tickets:
        start, end = ticket
        path[start].append(end)

    dfs("ICN", path, [], ans, len(tickets))
    return sorted(ans)[0]


tickets = [
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
]
print(solution(tickets))
