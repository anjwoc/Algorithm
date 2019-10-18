mylist = [3, 2, 6, 7]
ret = [i**2 for i in mylist if i%2 == 0]
print(ret)

tmp = [] 
for x in range(10):
    tmp.append(x**2)
# 위 방법은 x라는 이름의 변수를 만들고 루프가 종료된 후에도 남아있게 된다.
tmp = list((map(lambda x: x**2, range(10))))
print(tmp)
# 위와 같이 만들게되면 어떠한 부작용도 없이 만들 수 있다
tmp = [x**2 for x in range(10)]
print(tmp)

#아래 예제는 두 리스트가 서로 같지 않은 것 끼리 결합
tmp = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]
print(tmp)

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!= y:
            combs.append((x,y))
print(combs)

# 리스트 컴프리헨션이 복잡한 표현식과 중첩된 함수들을 포함할 때
from math import *
tmp = [str(round(pi, i)) for i in range(1, 16)]
print(tmp)

# 중첩된 리스트 컴프리헨션
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
tmp = [[row[i] for row in matrix] for i in range(4)]
print(tmp)