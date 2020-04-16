import sys
import copy

input = lambda: sys.stdin.readline().strip()


def solution(numbers=[1, 2, 3, 4, 5], target=3):
    ans = 0
    op_list = []

    def generate(arr, op_len):
        if len(arr) == op_len:
            op_list.append(copy.deepcopy(arr))
            return

        arr.append("+")
        generate(arr, op_len)
        arr.pop()

        arr.append("-")
        generate(arr, op_len)
        arr.pop()

    generate([], len(numbers))
    # for op in op_list:
    #     string = ""
    #     for i in range(len(op)):
    #         string += int(op[i] + str(numbers[i]))
    #     print(string)
    #     if eval(string) == target:
    #         ans += 1
    for op in op_list:
        tmp = 0
        for i in range(len(op)):
            tmp += int(op[i] + str(numbers[i]))
        if tmp == target:
            ans += 1

    return ans


print(solution())
