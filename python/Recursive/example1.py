def func(n):
    print(n)
    #n==1일때 return한다는 base condition이다.
    if(n==1):
        return
    func(n-1)

func(5)

