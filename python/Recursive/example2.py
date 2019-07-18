def func(n):
    #여기서도 n==1일때 1을 return 시키는 base condition
    if(n==1):
        return 1
    return n*func(n-1)

print(func(5))
