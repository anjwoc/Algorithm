def solution(arr):
    answer = []
    answer.append(arr[0])
    cmp = arr[0]
    for i in range(1,len(arr),1):
        if(cmp == arr[i]):
            continue
        else:
            answer.append(arr[i])
            cmp = arr[i]

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return answer


arr = [1,1,3,3,0,1,1]
#answer = [1,3,0,1]
arr2 = [4,4,4,3,3]
#answer = [4,3]
arr3 = [1,3,3,7,5,9,9,13]
#print(solution(arr))

#print(solution(arr2))
print(solution(arr3))

#다른 사람 풀이
def no_continuous(s):
    ret = []
    for i in s:
        if ret[-1:] == [i]: continue
        #ret[-1:]은 가장 뒤의 원소를 리스트로 만들어준다. 그래서 [i]로 리스트형태로 비교해야한다.
        #리스트를 슬라이싱하면 그대로 리스트를 리턴
        ret.append(i)
    return ret
print(no_continuous("133303"))