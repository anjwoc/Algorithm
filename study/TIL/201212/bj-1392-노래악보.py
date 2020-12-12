import sys
input = sys.stdin.readline

n, q= map(int, input().split())
# 1번 악보부터 N번 악보까지 차지하는 시간
T = [int(input()) for _ in range(n)] 
# 알고자 하는 Q개의 시간
Q = [int(input()) for _ in range(q)]

'''
각 악보들이 따라 부르는데 걸리는 시간
예제 입력의 경우 1번악보: 1, 2번악보: 2, 3번악보: 5가 나오고
Q의 시간이 4인 경우 2보다 크고 5보다 작으므로 3번 악보가 된다.
'''
ranges = [-1 for _ in range(n)]
for i in range(n):
  for j in range(i+1):
    ranges[i] += T[j]

for q in Q:
  for i in range(n):
    if i == 0 and q <= ranges[0]:
      print(1)
    elif i>0 and ranges[i-1] < q <= ranges[i]:
      print(i+1)
    
    
    




