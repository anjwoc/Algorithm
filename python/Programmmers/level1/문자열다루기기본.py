def solution(s):
    check = s.isdigit()
    
    if(check == True and (len(s)==4 or len(s)==6)):
       answer=True
    else:
       answer=False

    return answer

#다른 사람 코드
def solution2(s):
    return s.isdigit() and len(s) in (4,6)

