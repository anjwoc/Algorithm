plus_ten = lambda x : x+10
print(plus_ten(10))
#���� ǥ���� ��ü�� ȣ���ϴ� ���
print((lambda x:x+20)(10))

#��� ����1 : ���� ǥ������ �μ��� ����ϱ�
ex1 = list(map(plus_ten, [1,2,3]))
print(ex1)
#�� �ٷ� ���ϼ� �ִ�.
print(list(map(lambda x:x+10, [1,2,3])))

#��� ����2 : ���� ǥ���Ŀ� ���Ǻ� ǥ���� ����ϱ�
#lambda �Ű����� : ��1 if ���ǽ� else ��2
a = [1,2,3,4,5,6,7,8,9,10]
ex2 = list(map(lambda x: str(x) if x%3 == 0 else x, a))
print(ex2)
ex3 = list(map(lambda x: str(x), a))
print(ex3)

#��� ����3 : map�� ��ü�� ���� �� �ֱ�
#map�� ����Ʈ ���� �ݺ�������(iterable)�� ��ü�� ���� �� ���� �� �ִ�.
a = [1,3,5,7,9]
b = [2,4,6,8,10]
ex4 = list(map(lambda x,y: x*y, a,b))
print(ex4)

