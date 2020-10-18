# 최소 공배수
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# 나눗셈 할 때 주의점
print(3 / 3)  # 1.0
print(3 // 3)  # 1
print(divmod(7, 3))  # a를 b로 나눈 (몫, 나머지)
# 작은 숫자인 경우는 divmod가 더 느리고 큰 숫자인 경우는 divmod가 더 빠르다.

# 유리수를 사용할 때는 튜플 형태로 저장해서 사용하면 좋음
# 1/3
a = (1, 3)

# case 1
s = ''
for i in range(10000):
    s += str(i)

# case2
s2 = ''
s2 = s2.join([str(i) for i in range(10000)])

# 데이터의 개수가 늘어날수록 join을 이용하는 2번 방법이 더 빠르다.

arr = [1, 2, 3, 4]
arr[0:0] = [4]
arr[1:1] = [3]

arr[1:2] = [5]
print(arr)

# number to ascii code
print(chr(65))

# ascii code to number
print(ord('A'))

# short circuit
# 0으로 나누면 발생하는 divide by zero 에러가 우선순위로 발생하지 않는다.
# and 연산으로 앞의 조건이 거짓이면 뒤의 항은 무시가 되고
if 0 and 1//0:
    print()
# or 연산으로 앞 조건이 참이면 뒷 조건이 무시가 된다.
if 1 or 1//0:
    print()


# 중복 체크
def check(lst):
    return len(lst) == len(set(lst))
