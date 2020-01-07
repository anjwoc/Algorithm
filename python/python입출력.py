import sys

'''
input()으로는 시간초과가 뜨는 문제들이 readline()으로 받으면
통과되는 경우가 많다.
속도는 sys.stdin.readline() > raw_input() > input()
'''
sys.stdin.readline()


'''
여러 라인을 입력받을 때는 아래와 같이 사용
'''

n = input()
a = [sys.stdin.readline() for i in range(n)]
# a = ["1 2 3 ", "4 5 6"]

#재귀 함수가 있는경우 최대 깊이를 설정
'''
DFS/BFS의 경우 C, C++의 경우는 문제 없지만
python에서는 런타임 에러가 뜨는 경우가 자주 생긴다.
재귀 허용깊이를 수동으로 늘려주는 코드를 삽입해야함
'''
sys.setrecursionlimit(10**8)

'''
위의 것들을 다해도 안되면 pypy로 제출을 해야하는데
주의할 점은 pypy는 setrecursionlimit이 먹히지 않는다.
임의로 재귀의 깊이를 설정하는게 불가능
'''
