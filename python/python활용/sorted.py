#원본을 유지한채, 정렬된 리스트 구하기
'''
sorted()를 모르면 원본을 유지한채 리스트를 구하려면
list1 = [3,2,1]
list2 = [i for i in list] 아니면 copy.deepcopy
list2.sort()
'''
list1 = [3,2,1]
list2 = sorted(list1)

list3 = ['B', 'a', 'C']
list4 = sorted(list3)
print(list4)