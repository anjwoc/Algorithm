'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
'''
def solution(arr, divisor):
    answer = [val for val in arr if(val%divisor==0)]
    answer.sort()
    if(len(answer)==0): return [-1]
    return answer


arr = [5, 9, 7, 10]	
divisor = 5

print(solution(arr, divisor))

#다른 사람 풀이
def solution2(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr)!=0 else [-1]

print(solution2(arr,divisor))

def solution3(arr, divisior): return sorted([val for val in arr if val%divisor==0]) or [-1]
