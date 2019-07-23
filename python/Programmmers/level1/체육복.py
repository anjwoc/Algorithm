def solution(n, lost, reserve):
    ret = 0
    #모두다 옷을 가지고 있다.
    all_list = [1]*n

    #여분의 옷이 있는 사람 표시
    for i in reserve:
        all_list[i-1] = 2

    #옷을 잃어버린 사람 표시
    for i in lost:
        all_list[i-1] = all_list[i-1]-1

    for idx, val in enumerate(all_list):
        if(idx>0 and val==0 and all_list[idx-1] == 2):
            all_list[idx] = 1
            all_list[idx-1] -= 1
        if(idx<n-1 and val==0 and all_list[idx+1] == 2):
            all_list[idx] = 1
            all_list[idx+1] -=1
    #1의 개수를 카운트한 것을 리턴하면 리스트에 2인 값도 있어서 제대로된 결과가 안나온다.
    return n-all_list.count(0)

n = 5
reserve = [1,3,5]
lost = [2,4]
print("ret : "+str(solution(n, lost, reserve)))

def another_solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    print(_reserve)
    _lost = [l for l in lost if l not in reserve]
    print(_lost)
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
print("another : "+str(another_solution(n, lost, reserve)))