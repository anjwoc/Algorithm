#answer = [[0 for i in range(len(mylist))] for j in range(len(mylist[0]))]
#일반적인 경우
# for i in range(len(mylist[0])):
#     for j in range(len(mylist)):
#         answer[i][j] = mylist[j][i]
'''
zip(*iterables)는 각 iterables 의 요소들을 모으는 이터레이터를 만든다.
튜플의 이터레이터를 돌려주는데, i번째 튜플은 각 인자로 전달된 시퀀스나 이터러블의 i번째 요소로 포함합니다.
'''
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))

#List Comprehension
tmp1 = [list(a) for a in zip(*mylist)]
#반면에 list comprehension을 쓰면 형 변환을 따로 해줄 필요가 없다.
#Map
tmp2 = list(map(list, zip(*mylist)))
#map 함수는 iterator를 반환하기 때문에 list든 어떤 형태로 변환해야 한다.


mylist2 = [1,2,3]
new_list2 = [40,50,60]
for i in zip(mylist2, new_list2):
    print(i)

#zip의 사용 예1) 여러 개의 iterable을 동시에 순회할 때 사용
list1 = [1,2,3,4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
    print(i+j+k)

#zip의 사용 예2) key 리스트와 value 리스트로 딕셔너리 생성하기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer)