"""
해시, 배열, 구현
"""

n = int(input())

arr1 = set(map(int, input().split()))
"""
arr1 = {}
for i in list(map(int, input().split())):
    arr1[i] = True
"""

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i not in arr1:
        print(0)
    else:
        print(1)

"""
python에서 in 연산자의 시간복잡도는 list or tuple에서 O(n)의 복잡도를 가진다.
일일히 다 확인해야 하기 때문에 너무 느려서 이 문제를 in 연사자를 통해 해결하면 시간초과가 나오니
dictionary로 해시 구조를 이용해 풀어야한다.

아니면 set을 이용하는 것도 가능하다.

두 방법으로 모두 풀어보니 속도는 근소하게 set이 조금 더 빨랐다.
"""
"""
해시를 이용한 풀이
for i in arr2:
    try:
        if arr1[i]:
            print(1)
    except:
        print(0)
"""
