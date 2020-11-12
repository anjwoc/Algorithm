import sys
input: lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
team_mem, mem_team = {}, {}

for _ in range(n):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for _ in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name


for _ in range(m):
    name, q = input(), int(input())

    if q:
        # 1
        print(mem_team[name])
    else:
        # 0
        for val in sorted(team_mem[name]):
            print(val)
