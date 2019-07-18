import sys
a, b, c = map(int, sys.stdin.readline().split())

def d(a,b):
    if(b==0):
        return 1
    elif(b==1):
        return a
    elif(b%2 > 0):
        return d(a,b-1)*a
    h = d(a, b//2)
    h%=c
    return h**2%c

print(d(a,b)%c)