import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = []
for i in range(1, n + 1):
    arr.append((i, list(input().split())))

ans = sorted(arr, key=lambda a: (int(a[1][0]), int(a[0])))
"""
python sorted lambda multiple key
sorted에서 key값을 여러 개주는 방법은 tuple의 형태로 인자를 두개 넘겨주는데
여기서 나이순으로 오름차순, 만약에 나이가 같다면 가입한 순으로 정렬해야하니
a[1][0] => 나이, a[0] 가입한 순서대로 넣은 i값을 기준으로 한다.
만약 해당 부분들을 나이는 내림차순으로 가입한 순서만 오름차순으로 하고싶다면
(-a[1][0], a[0])로 하면된다.
"""
for i in ans:
    print(*i[1])
