def solution(A, B):
    ans = 0

    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        ans += a * b

    return ans
