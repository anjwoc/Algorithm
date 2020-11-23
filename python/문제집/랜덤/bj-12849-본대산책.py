import sys
input = sys.stdin.readline

# 총 7개의 건물이 있으므로 각각의 건물에 도착하는 경우의 수
# 0분에 어떤 지점에 도착할 수 있는 상태


def next_position(state):
    tmp = [0 for _ in range(8)]
    # 정보과학관까지 오려면 전산관이나 미래관에서 1분전에 와야한다.
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    return tmp


# 0: 정보과학관
# 1: 전산관
# 2: 미래관
# 3: 신앙관
# 4: 한경직
# 5: 진리관
# 6: 학생회관
# 7: 형남공학관
dp = [1, 0, 0, 0, 0, 0, 0, 0]


for i in range(int(input())):
    dp = next_position(dp)

print(dp[0] % 1000000007)
