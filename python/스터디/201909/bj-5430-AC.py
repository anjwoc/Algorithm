import sys
input: lambda : sys.stdin.readline().strip()

'''
R(뒤집기), D(버리기)
R은 배열을 역순으로 뒤집고 D는 첫 번째 요소를 제거
배열이 빈 상태에서 D를 사용하면 에러
'''

def R(S):
    # reverse함수는 O(n)으로 돌기때문에 시간초과
    # array[::-1]은 역순으로 출력하는 슬라이싱

    arr = S[1:len(S)-1]
    arr = '[' + arr + ']'
    return arr

def D(S):
    # 숫자만 추출 -> ','을 기준으로 분리 -> 첫 요소를 제외한 나머지를 리스트로
    arr = S[1:len(S)-1].split(',')[1:]
    
    if len(arr)-2 >= 0:
        return '[' + ','.join(arr) + ']'
    else:
        return 'error'

    
def make(S):
    if S == 'error':
        return S
    arr = '[' + S[1:len(S)-1] + ']'
    return ''.join(arr)


for _ in range(int(input())):
    ops = list(input())
    n = int(input())
    arr = input()
    
    for op in ops:
        if op == 'R':
            arr = R(arr)
        elif op == 'D':
            arr = D(arr)
    
    print(make(arr))
            