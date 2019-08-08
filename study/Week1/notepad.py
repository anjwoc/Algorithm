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
    
    return ret

def check(cmp):
    global cnt
    print()
    tetrisHeights = list(map(int, cmp))
    n = len(tetrisHeights)
    size = c-n+1
    for i in range(0, size, 1):
        diff = abs(tetrisHeights[0] - heights[i])
        ok = True
        for j in range(n):            
            if abs(tetrisHeights[j] - heights[i+j]) != diff:
                ok=False
                break
        if ok:
            cnt+=1
    # for i in range(c-n):
    #     # if((i+len(cmp)) > c):
    #     #     break
    #     tmp = heights[i:i+n]
    #     #print("tmp: " + str(tmp) + "tetris: "+str(tetrisHeights))
    #     sub = subtract(tmp, tetrisHeights)
    #     #중복제거해서 전체 개수가 1이면 일정하기 때문에 +1
    #     if(len(list(set(sub))) != 1):
    #         continue
    #     else:
    #         cnt+=1

        

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
        check('00')
        check('110')
        check('02')
        
solve(p)
print(cnt)