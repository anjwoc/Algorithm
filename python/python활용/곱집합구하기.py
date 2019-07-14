import itertools
from itertools import count
from functools import reduce
import operator
#Cartesion Product
iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

for i in iterable1:
    for j in iterable2:
        for k in iterable3:
            print(i+j+k)

#위는 일반적인 방법
a = list(map(str, itertools.product(iterable1, iterable2, iterable3)))
print(list(itertools.product(iterable1, iterable2, iterable3)))

letters = ['a', 'b', 'c', 'd', 'e', 'f']
booleans = [1, 0, 1, 0, 0, 1]
decimals = [0.1, 0.7, 0.4, 0.4, 0.5]
#chain()은 간단히 리스트(lists, tuples, iterables)를 연결하는 것이다.
print(list(map(''.join, itertools.chain(letters, booleans, decimals))))
print(list(itertools.chain(letters, booleans, decimals)))

#count()는 반복하고자 하는 count(start, step) step만큼씩 증가한다.
for num, letter in zip(count(0,10), ['a', 'b', 'c', 'd', 'e']):
    print('{0}: {1}'.format(num, letter))


#2차원을 1차원으로 만드는 방법
my_list = [[1, 2], [3, 4], [5, 6]]

#방법 1) sum 함수
answer = sum(my_list, [])
print("#1: " + str(answer))
'''
sum([[1,2],[3,4],[5,6]], [])을 호출하면 
1. start(=[]) + [1,2] + [3,4] + [5,6]을 계산해서 
2. [1,2,3,4,5,6]을 리턴한다.
'''

#방법 2) itertools.chain()
answer = list(itertools.chain.from_iterable(my_list))
print("#2: "+str(answer))

#방법 3) itertools와 unpacking
answer = list(itertools.chain(*my_list))
print("#4: "+str(answer))

#방법 4) list comperehension 
answer = [element for array in my_list for element in array]
print("#3: "+str(answer))

#방법 5) reduce 함수 이용1
answer = list(reduce(lambda x,y : x+y, my_list))
print("#5: "+str(answer))

#방법 6) reduce 함수 이용2
answer = list(reduce(operator.add, my_list))
print("#6: "+str(answer))