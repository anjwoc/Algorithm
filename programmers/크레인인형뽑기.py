def solution(board, moves):
    stacks = []
    ans = 0

    def push(st, item):
        if len(st) > 0 and st[-1] == item:
            st.pop()
            return 2

        st.append(item)
        return 0

    for move in moves:
        idx = int(move) - 1
        for x in range(len(board[0])):
            cur = board[x][idx]
            if cur == 0:
                continue
            else:
                num = push(stacks, board[x][idx])
                board[x][idx] = 0
                ans += num
                break

    return ans
