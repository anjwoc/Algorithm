plus_ten = lambda x : x+10
print(plus_ten(10))
#람다 표현식 자체를 호출하는 방법
print((lambda x:x+20)(10))

#사용 예제1 : 람다 표현식을 인수로 사용하기
ex1 = list(map(plus_ten, [1,2,3]))
print(ex1)
#한 줄로 줄일수 있다.
print(list(map(lambda x:x+10, [1,2,3])))

#사용 예제2 : 람다 표현식에 조건부 표현식 사용하기
#lambda 매개변수 : 식1 if 조건식 else 식2
a = [1,2,3,4,5,6,7,8,9,10]
ex2 = list(map(lambda x: str(x) if x%3 == 0 else x, a))
print(ex2)
ex3 = list(map(lambda x: str(x), a))
print(ex3)

#사용 예제3 : map에 객체를 여러 개 넣기
#map은 리스트 등의 반복가능한(iterable)한 객체를 여러 개 넣을 수 있다.
a = [1,3,5,7,9]
b = [2,4,6,8,10]
ex4 = list(map(lambda x,y: x*y, a,b))
print(ex4)

