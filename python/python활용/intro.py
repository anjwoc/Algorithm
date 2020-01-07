def solution(mylist):
    return list(map(len, mylist))

arr = [[1,2], [2,3]]

print(solution(arr))

'''
iterable: 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체이다. list, str, tuple, dict등이 여기에 속함
sequence: int 타입 인덱스를 통해, 원소에 접근할 수 있는 iterable입니다. iterable의 하위 카테고리라고 생각하면 된다.
list, str, tuple이 여기 속합니다.
(dictionary는 다양한 타입을 통해 원소에 접근할 수 있기 때문에 sequence에 속하지 않습니다.)
packing : 여러개의 객체를 하나의 객체로 합쳐준다.
unpacking: 여러개의 객체를 포함하고 있는 하나의 객체를 풀어준다.
'''



