#데크는 Double-ended queue의 줄임말
'''
즉 양방향에서 데이터를 처리할 수 있는 queue형 자료구조를 의미한다.
python에서 collections.deque는 list와 비슷하다.
append(), pop()등의 메소드는 deque에서도 제공 
append는 deque의 오른쪽(마지막)에 추가해준다.
쉽게말하면 스택과 큐의 기능을 한번에 가진 자료구조
'''
from collections import deque
dq = deque('apple')
#스택 구현
#스택은 마지막(오른쪽 끝)으로 입출력한다. 입력 시에는 append를 출력 시에는 pop을 사용
dq.append('m')
print(dq.pop())

#큐 구현
#큐는 왼쪽(처음)에서 입력되고, 오른쪽(마지막)에서 출력된다.
'''
오른쪽 출력 시에는 위와 동일하게 pop을 사용하고 왼쪽 값에 입력을 할 때는 appendleft()메소드 사용
반대로 오른쪽에 넣고 싶으면 append(), 왼쪽에서 값을 빼고 싶으면 popleft()를 사용한다.
'''

