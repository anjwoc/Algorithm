'''
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요. 
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
'''
def solution(a, b):
    ret = 0
    if(a>b):
        a,b = b,a
    for i in range(a,b+1,1):
        ret+=i
    return ret

#다른 사람 풀이
def solution2(a,b):
    if a>b: a,b = b,a
    return sum(range(a,b+1))


print(solution(3,5))