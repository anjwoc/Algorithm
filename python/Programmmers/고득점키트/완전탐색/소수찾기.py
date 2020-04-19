import math
import itertools


# def get_primes(n):
#     is_primes = [True] * n
#     # n의 최대약수는 sqrt(n) 이하이므로 계산 후, 소수점이 있으면 올림으로 최대 반복 횟수 계산
#     max_len = math.ceil(math.sqrt(n))

#     for i in range(2, max_len):
#         # True일 경우 소수
#         if is_primes[i]:
#             for j in range(i + i, n, i):
#                 is_primes[j] = False

#     return [i for i in range(2, n) if is_primes[i]]


def solution(numbers):
    ans = 0
    items = list(numbers)
    # primes = get_primes(9999999)
    arr = []

    for i in range(1, len(items) + 1):
        for val in list(itertools.permutations(items, i)):
            arr.append(int("".join(val)))
    print(arr)
    arr = list(set(arr))
    if arr.count(1):
        arr.remove(1)
    if arr.count(0):
        arr.remove(0)

    for x in arr:
        i = 2
        while i * i <= x:
            if x % i == 0:
                ans -= 1
                break

            i += 1
        ans += 1
    return ans


print(solution("011"))
