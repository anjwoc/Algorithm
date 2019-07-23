def solution(s):
    idx = len(s)//2
    if(len(s)%2 == 0):
        #짝수
        print(s[idx-1:idx+1])
        
    if(len(s)%2 == 1):
        #홀수
        print(s[idx])

    answer = ''
    return answer


s1 = "abcde"
s2 = "qwer"
s3 = "qwertw"
print(solution(s1))
print(solution(s2))
print(solution(s3))

def string_middle(str):
    print((len(str)-1)//2)
    print(len(str)//2+1)
    return str[(len(str)-1)//2 : len(str)//2+1]

print(string_middle("power"))