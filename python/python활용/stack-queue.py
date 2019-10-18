'''
리스트를 스택으로 사용하기
스택의 꼭대기에 마지막 항목을 넣을때는 append, 꼭대기의 마지막 값을 꺼낼 때는 pop
LIFO
'''
st = [3,4,5]
st.append(6)
st.append(8)
print(st)
st.pop()
print(st)

'''
리스트를 큐로 사용하기
리스트는 이 목적에는 효율적이지 않다. 끝에 덧붙이거나, 끝에서 꺼내는 것은 빠르지만, 헤드에 덧붙이거나
헤드에서 꺼내는 것은 느리다(다른 요소들을 모두 한 칸씩 이동시켜야 하기 때문에)
그래서 collections.deque를 사용
FILO
'''
from collections import deque
que = deque([1, 2, 3])
que.append("Terry")
que.append("Graham")
que.popleft()
print(que)
que.popleft()
print(que)