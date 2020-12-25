def solution(prices):
    ans = [0]*len(prices)

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                ans[i] += 1
            else:
                ans[i] += 1
                break

    return ans
