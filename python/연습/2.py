# def persistence(n):
#     tmp = list(str(n))
#     ans = 0
#     while len(tmp) > 1:
#         ans += 1
#         mul = 1
#         for i in tmp:
#             mul *= int(i)
#         tmp = list(str(mul))

#     return ans

from functools import reduce
import operator


def persistence(n):
    ans = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        ans += 1
    return ans


print(persistence(39))
