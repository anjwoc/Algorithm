import sys

c, p = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
cnt = 0

def subtract(tmp1, tmp2):
    ret = []
    if(len(tmp1) != len(tmp2)):
        return
    else:
        for i in range(len(tmp1)):
            ret.append(abs(tmp1[i] - tmp2[i]))
    return list(set(ret))

def check(cmp):
    global cnt
    tetrisHeights = list(map(int, cmp))
    n = len(tetrisHeights)
    size = c-n+1
    for i in range(0, size, 1):
        h = heights[i:i+n]
        sub = subtract(h, tetrisHeights)
        #중복제거해서 전체 개수가 1이면 높이가 일정하기 때문에 +1
        if(len(sub) != 1):
            continue
        else:
            cnt+=1

def solve(p):
    if(p==1):
        check('0')
        check('0000')
    elif(p==2):
        check('00')
    elif(p==3):
        check('001')
        check('10')
    elif(p==4):
        check('100')
        check('01')
    elif(p==5):
        check('000')
        check('01')
        check('101')
        check('10')
    elif(p==6):
        check('000')
        check('00')
        check('011')
        check('20')
    elif(p==7):
        check('000')
        check('110')
        check('00')
        check('02')
        
solve(p)
print(cnt)