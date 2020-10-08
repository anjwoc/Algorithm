n = int(input())
k = int(input())

if k >= n:
    # 해당 케이스를 처리안해주면 런타임 에러가 발생
    # 타 언어도 마찬가지
    print(0)
    exit()

data = list(map(int, input().split()))
lst = []
data.sort()

for i in range(1, n):
    lst.append(data[i] - data[i - 1])

lst.sort(reverse=True)

for i in range(k - 1):
    lst[i] = 0
result = sum(lst)

print(result)