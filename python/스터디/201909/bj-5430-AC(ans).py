import sys
input: lambda : sys.stdin.readline().strip()

'''
R(뒤집기), D(버리기)
R은 배열을 역순으로 뒤집고 D는 첫 번째 요소를 제거
배열이 빈 상태에서 D를 사용하면 에러
'''

for _ in range(int(input())):
    ops = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    R = 0
    front = 0
    back = 0

    ops.replace('RR', '')
    for op in ops:
        if op == 'R':
            R += 1
        elif op == 'D':
            if R % 2 == 0:
                front += 1
            else:
                back += 1
    
    if front + back > n:
        print('error')
        continue

    nums = arr[front:n-back]

    if R % 2 == 1:
        print('[' + ','.join(nums[::-1]) + ']')
    else:
        print('[' + ','.join(nums) + ']')