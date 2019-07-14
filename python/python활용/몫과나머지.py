#숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.
a , b = map(int , input().strip().split())
#strip()함수는 양쪽 끝에 있는 공백과 \n기호를 삭제시켜 준다.
#print(' '.join(map(str, [int(a/b), int(a%b)])))
print(*divmod(a,b))
#divmod는 작은 숫자를 다룰 때는 a//b, a%b보다 느리다. 대신 큰 숫자를 다룰 때는 divmod가 더 빠르다.