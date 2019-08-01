import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
e = 0
ans = 0
check = [False]*n
def solve(cnt, e):
    global ans
    if(cnt==n-2):
        ans = max(ans, e)
        return
    for i in range(1, n-1):
        if not check[i]:
            left, right = i-1, i+1
            while(check[left] and left>0):
                left -= 1 
            while(check[right] and right<n-1):
                right += 1
            check[i] = True
            solve(cnt+1, e+(w[left]*w[right]))
            check[i] = False
        
solve(0, 0)
print(ans)