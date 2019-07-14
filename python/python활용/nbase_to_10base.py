#n진법으로 표기된 string을 10진법 숫자로 변환하기
'''
base 진법으로 표기된 숫자를 10진법 숫자로 출력해보세요
'''
#string[::-1] 문자열 뒤집기
#base ** idx 는 base의 idx 제곱 승
#num, base = map(int, input().strip().split())
num = '3212'
base = 5
answer = 0

#일반 적인 경우
for idx, i in enumerate(num[::-1]):
    print("i: "+str(i))
    answer += int(i) * (base ** idx)
    print(answer)

print("result: "+str(answer))

'''
하지만 파이썬에서는 int(x, base=10) 함수는 진법 변환을 지원한다.
이 기본적인 함수를 잘 쓰면 코드를 짧게 쓸 수 있고, 또 시간을 절약할 수 있다.
'''
answer = int(num, base)
print(answer)