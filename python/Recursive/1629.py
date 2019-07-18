import sys
import math
sys.setrecursionlimit(10000)
a, b, c = map(int, sys.stdin.readline().split())
#a를 b번 곱한 수를 알고싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램

def pow_mod(a, b, c):
    if(b==0):
        return 1
    ret = pow_mod(a, b/2, c)
    ret = ret*ret%c
    if(b%2==0):
        return ret
    return ret*a%c

print(pow_mod(a,b,c))
