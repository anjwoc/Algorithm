import string
num = int(input().strip())
#입력으로 0이들어오면 소문자 1이들어오면 대문자로 사전 순으로 출력
if(num ==0):
    print(string.ascii_lowercase)
else:
    print(string.ascii_uppercase)
