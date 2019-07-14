import collections
#가장 많이 등장하는 알파벳 찾기 - Counter

#어떤 원소 x가 주어진 시퀀스타입에 몇 번이나 등장하는지 세야 할 때가 있다.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
print(collections.Counter(my_list))


