import re
str1 = 'hello world'
str2 = 'world'
idx = str1.find(str2)
#찾은 특정 문자열의 시작 인덱스를 반환한다.
#없으면 -1 리턴
print(str1[idx])

str1 = 'hello world! world world'
str2 = 'world'
idx = str1.find(str2)
print(idx)
while str1[idx+1:].find(str2) != -1:
    idx = str1[idx+1:].find(str2)+idx+1
    print(idx)

for a in re.finditer(str2, str1):
    print(a.start())


#정규식을 이용한 문자열 검색
'''
match() : 문자열의 처음부터 정규식과 매치되는지 조사
search() : 문자열 전체를 검색하여 정규식과 매치되는지를 조사
findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
finditer() : 정규식과 매치되는 모든 문자(substring)열을 반복 가능한(iterable) 객체로 돌려준다.

match 객체란 정규식의 검색 결과로 돌려주는 객체
'''
#패턴을 만든다.
p = re.compile('[a-z]+')
print(p)

m = p.match("python")
k = p.match("3 python")
#3 python은 시작인 3이 a-z에 부합되지 않아 None 리턴
print(m.start())
print(m.end())
print(m.span())





