import sys
input: lambda: sys.stdin.readline().strip()

dic = {}
for _ in range(int(input())):
    data = input()
    if data not in dic:
        dic[data] = 1
    else:
        dic[data] += 1

'''
이유는 모르겠는데 오답
arr = sorted(dic.keys(), key=lambda x: x[1], reverse=True)
print(sorted(arr)[0])
'''
target = max(dic.values())

arr = []
for book, number in dic.items():
    if number == target:
        arr.append(book)

print(sorted(arr)[0])
