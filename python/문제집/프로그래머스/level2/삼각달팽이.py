def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    last = sum(range(1, n+1))
    acc = 1
    for i in range(n):
        flag = False
        # 세로
        for j in range(i, n-i):
            if arr[i][j] != 0:
                continue
            arr[j][i] = acc
            if acc == last:
                flag = True
                break
            acc += 1

        if flag:
            break

        # 가로
        for j in range(i, n-i):
            if arr[i][j] != 0:
                continue
            arr[n-i-1][j] = acc
            if acc == last:
                flag = True
                break
            acc += 1

        if flag:
            break

#         # 대각선
        for k in range(n-i-1, i, -1):
            if arr[k][k] != 0:
                continue
            arr[k][k] = acc
            if acc == last:
                flag = True
                break
            acc += 1

        if flag:
            break

    for i in arr:
        print(i)

    ans = []
    for i in arr:
        ans += list(filter(lambda x: x != 0, i))
    return ans


inputs = [4, 5, 6]
answers = [
    [1, 2, 9, 3, 10, 8, 4, 5, 6, 7],
    [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9],
    [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
]

for i in range(3):
    print("----%d----" % (i))
    ans = solution(inputs[i])
    print('출력')
    print(ans)
    print('정답')
    print(answers[i])

    if ans == answers[i]:
        print("Success")
    else:
        print("Fail")
    print("----%d----" % (i))
