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

    # 나눗셈 연산을 미리 하는 쪽이 시간이 훨씬 빠르다.
    # 미리 하지 않은 경우는 약 4000ms 미리 한 경우는 360ms
    # 이유는 나눗셈 연산이 모든 연산 중 무거운 연산에 속한다.
    # 파이썬같은 경우는 수가 더해지는 것이 클 수록 시간 복잡도가 오래 걸린다.
    # 그러므로 나눗셈을 많이 하는것이 좋지는 않지만
    # 덧셈을 하는데 걸리는 시간이 줄어들고 장기적으로 봤을 때 더 효율적인 방법
    # 덧셈을 더 빠르게 하는 용도로 미리 나눠주는 방법이다.
    for i in range(8):
        tmp[i] %= 1000000007
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

print(dp[0])
