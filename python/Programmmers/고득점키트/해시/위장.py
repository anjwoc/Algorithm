from collections import Counter

data1 = [
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
data2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]


def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    print(c)
    for v in c.values():
        answer *= v + 1  # 아무것도 입지 않은 조건
    answer -= 1  # 최소한 하나의 의상을 착용하기 때문에 모든 의상종류를 착용하지 않은 조건
    return answer
    
def solution(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

print(solution(data2))
