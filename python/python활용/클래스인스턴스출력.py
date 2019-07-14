'''
인스턴스 출력 형식을 지정하는 방법
ex) 2차원 평면 위의 점을 나타내는 coord 클래스의 인스턴스를 (x, y)로 출력하기
다른 언어에서 or 이 기능을 모르면 일반적으로 출력 함수를 만들거나, print문 안에서 format 지정
'''

class Coord(object):
    def __init__(self ,x, y):
        self.x, self.y = x,y
point = Coord(1,2)
print(point)
print( '({}, {})'.format(point.x, point.y) )
#or 아래와 같이 활용
def print_coord(coord):
    print( '({}, {})'.format(coord.x, coord.y) )
print_coord(point)

#파이썬에서는 __str__메소드를 사용해서 class 내부에서 출력 format을 지정할 수 있다.
class Coord(object):
    def __init__(self, x, y):
        self.x , self.y = x, y
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
    #__str__메소드로 따로 출력 함수를 만들지않아도 된다.
point = Coord(1,2)
print(point)