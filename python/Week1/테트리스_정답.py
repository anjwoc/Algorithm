import sys

c, p = map(int, sys.stdin.readline().split())
heights = list(map(int, sys.stdin.readline().split()))
cnt = 0

def solve(p):
    ret = 0

    if(p==1):
        ret = check('0') + check('0000')
    elif(p==2):
        ret = check('00')
    elif(p==3):
        ret = check('001') + check('10')
    elif(p==4):
        ret = check('100') + check('01')
    elif(p==5):
        ret = check('000') + check('01') + check('101') + check('10')
    elif(p==6):
        ret = check('000') + check('00') + check('011') + check('20')
    elif(p==7):
        ret = check('000') + check('110') + check('00') + check('02')

    print(ret)

def check(s):
    tetrisHeights = list(map(int, s))
    n = len(tetrisHeights)
    ret=0
    size = c-n+1
    for col in range(0, size, 1):
        ok = True
        diff = tetrisHeights[0] - heights[col]

        for i in range(n):
            if tetrisHeights[i] - heights[col+i] != diff:
                ok=False
                break
        if ok:
            ret+=1    
    return ret

solve(p)