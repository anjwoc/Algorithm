import sys
def nqueen(sol, n):
    global cnt
    if len(sol) == n:
        cnt+=1
        print(cnt, sol)
        return 0
    #0부터 n-1까지의 후보 배열로 만든다.
    candidate = list(range(n))
    for i in range(len(sol)):
        #같은 열에 놓이는지 체크
        if sol[i] in candidate:
            #같은 열에 놓이면 후보군에서 제외
            candidate.remove(sol[i])
        distance = len(sol)-i
        #같은 대각선 상(+)에 있는지 확인
        if sol[i] + distance in candidate:
            #같은 대각선 상에 있다면 후보에서 제외
            candidate.remove(sol[i]+distance)
        #같은 대각선 상에 있는지 확인
        if sol[i] - distance in candidate:
            candidate.remove(sol[i]-distance)
    if(candidate != []):
        for i in candidate:
            #후보의 요소를 정답 배열의 i+1로 추가
            sol.append(i)
            #재귀적으로 다음 행도 확인
            nqueen(sol, n)
            sol.pop()
    else:
        return 0

cnt=0
n = int(sys.stdin.readline())
for i in range(n):
    nqueen([i], n)

print(cnt)






