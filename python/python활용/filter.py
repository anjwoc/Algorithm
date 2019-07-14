from functools import reduce
'''
filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데,
filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옵니다.
'''
def f(x):
    return x>5 and x<10

a = [8,4,3,6,5,7,8,19,21]
test1 = list(filter(f,a))
print(test1)

'''
reduce함수
reduce는 반복 가능한(iterable) 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서
반환하는 함수다.(python3에서부터는 내장 함수가 아니다)
functools모듈에서 reduce함수를 가져와야한다. 
'''
def f2(x,y):
    return x+y
b=[1,2,3,4,5]
print(reduce(f2,b))

#람다식을 이용해서 만들어 보기
print(reduce(lambda x,y:x+y,a))

'''
map, filter, reduce와 리스트 표현식
리스트(딕셔너리, 셋) 표현식으로 처리할 수 있는 경우에는 map, filter와 람다 표현식
대신에 리스트 표현식을 사용하는 것이 좋다.
list(filter(lambda x:x >5 and x<10, a))
'''
c = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print([i for i in c if i>5 and i<10])
#리스트 표현식이 좀 더 알아보기 쉽고 속도도 빠르다.
#reduce도 for, while로 대체가능하면 for, while을 쓰자
#reduce는 가독성이 떨어저서 이런 이유로 python3에서부터 내장 함수에서 빠짐



