"""
2019 카카오 겨울 인턴십 문제
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
1,2번 테케틀림
"""


def pretty_print(arr):
    for i in arr:
        print(i)


def coordinates(arr):
    # 실수: 해당 컬럼이 모두 0이 되었을 경우 좌표가 비게되는데 이 경우 빈 배열이 리턴된다.
    pos = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[j][i] != 0:
                pos.append((j, i))
                break
            if j == len(arr[0]) - 1 and arr[j][i] == 0:
                pos.append((-1, -1))
                break

    return pos


def check_equal(stack):
    n1, n2 = stack[len(stack) - 1], stack[len(stack) - 2]
    if n1 == n2:
        return True
    return False


board, moves = (
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3],
        [0, 2, 5, 0, 1],
        [4, 2, 4, 4, 2],
        [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4],
)
# # board, moves = ([[0, 1], [1, 2]], [1, 2, 1, 2])

# stack = []
# ans = 0
# while moves:
#     cord = coordinates(board)
#     pos = moves.pop(0)  # 꺼낼 아이템
#     r, c = cord[pos - 1]
#     stack.append(board[r][c])
#     board[r][c] = 0
#     if len(stack) >= 2:
#         if check_equal(stack):
#             ans += 2
#             stack.pop()
#             stack.pop()
# print(ans)


def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer


print(solution(board, moves))
