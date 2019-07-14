'''
sequence type의 *연산
'''
n = int(input().strip())
for i in range(n):
    print('*'*(i+1))

#아래와 같은 식으로 앞의 리스트가 n번 반복되는 리스트를 만들 수 있다.
answer = [123, 456] * n
print(answer)

test = [[0]*10]*10
print(test)
