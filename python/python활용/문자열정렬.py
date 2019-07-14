s, n = input().strip().split()
n = int(n)
#일반적인 경우
answer = []
# for i in range(n-len(s)):
#     answer += ' '
# answer += s

#파이썬에서는 ljust, center, rjust와 같은 string 메소드를 사용해 코드를 줄일 수 있다.
answer.append(s.ljust(n)) #좌측 정렬
answer.append(s.center(n)) #가운데 정렬
answer.append(s.rjust(n)) #우측 정렬
for i in answer:
    print(i)
