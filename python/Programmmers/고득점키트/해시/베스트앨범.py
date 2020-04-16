import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


def solution(
    genres=["classic", "pop", "classic", "classic", "pop"],
    plays=[500, 600, 150, 800, 2500],
):
    result = []
    queue = [i for i in enumerate(zip(genres, plays))]
    list_geners = list(set(genres))
    # print(list_geners)
    count_genres = dict()
    for i in list_geners:
        count_genres[i] = 0
    for value in queue:
        count_genres[value[1][0]] += value[1][1]
    queue.sort(key=lambda x: (count_genres[x[1][0]], x[1][1], -x[0]))
    # {'pop': 3100, 'classic': 1450} 많이 재생된 장르로 먼저 수록하니까 이 값을 우선순위로 정렬하고(오름차순)
    # 다음은 장르 내에서 많이 재생된 노래(오름차순)
    # 다음은 고유번호가 낮은 노래를 먼저니까(내림차순)
    count_genres = count_genres.fromkeys(count_genres, 0)
    # fromkeys메소드로 count_genres를 다시 0으로 모두 초기화하고
    print(queue)
    try:
        while True:
            value = queue.pop()
            print(value)
            count_genres[value[1][0]] += 1
            if count_genres[value[1][0]] <= 2:
                result.append(value[0])
    except IndexError:
        pass
    return result


print(solution())
