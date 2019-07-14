#일반적으로 타 언어와 비슷하게 사용하면
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    raw = line.split()
    print(raw)
f.close()

'''
파이썬에서는 with - as 구문이 있어서 코드를 더 간결하게 사용 가능하다.
with - as 구문을 사용하면 file을 closeㅎ지 않아도 된다. 자동으로 close 됌
readlines가 EOF까지만 읽으므로, while문 안에서 EOF를 체크할 필요가 없다.
'''
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip.split('\t'))


