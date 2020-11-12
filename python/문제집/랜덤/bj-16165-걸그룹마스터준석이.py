import sys
input: lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = []

for _ in range(n):
    gname = input()
    dic = dict()
    dic[gname] = []
    for _ in range(int(input())):
        dic[gname].append(input())
    arr.append(dic)

for _ in range(m):
    qname = input()
    qcategory = int(input())

    if qcategory == 0:
        for target in arr:
            if qname in target.keys():
                for i in sorted(*target.values()):
                    print(i)
    elif qcategory == 1:
        for target in arr:
            key = list(*target.keys())[0]
            if qname in target[key]:
                print(key)
