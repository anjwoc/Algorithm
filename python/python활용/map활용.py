'''
일반 적인 경우
list1 = ['1', '100', '33']
list2 = []
for i in list1:
    list2.append(int(i))
'''
#모든 요소 형 변환
list1 = ['1', '100', '33']
list2 = list(map(int, list1))
print(list2)

#각 원소의 길이의 리스트를 리턴하는 방법
mylist = [[1, 2], [3, 4], [5]]
answer = list(map(len, mylist))
print(answer)