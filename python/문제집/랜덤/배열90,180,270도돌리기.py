
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

'''
input
4
1 2 3 2
3 8 7 2
8 2 3 1
3 4 5 1
'''


def pretty_print(A):
    print()
    for i in A:
        print(i)


def new_array(n):
    return [[0]*n for _ in range(n)]


'''
회전 전의 열 번호와 회전 후의 행 번호가 일치한다.
그리고 회전 후의 열은 N-1에서 회전 전의 행을 뺀 값과 같다.
'''


def rotate_right90(arr):
    ans = new_array(n)

    for i in range(n):
        for j in range(n):
            ans[j][n-i-1] = arr[i][j]
    return ans


pretty_print(rotate_right90(arr))


def rotate_left90(arr):
    ans = new_array(n)

    for i in range(n):
        for j in range(n):
            ans[n-j-1][i] = arr[i][j]
    return ans


pretty_print(rotate_left90(arr))


'''
회전 후의 행 번호는 N-1의 값에서 전의 행 번호를 뺀 것과 같고
회전 후의 열 번호는 N-1의 값에서 전의 열 번호를 뺀 것과 같다.
'''


def rotate_right180(arr):
    ans = new_array(n)

    for i in range(n):
        for j in range(n):
            ans[n-i-1][n-j-1] = arr[i][j]

    return ans


pretty_print(rotate_right180(arr))


# 270도는 왼쪽으로 90도와 동일하다.
def rotate_right270(arr):
    ans = new_array(n)

    for i in range(n):
        for j in range(n):
            ans[n-j-1][j] = arr[i][j]
    return ans
