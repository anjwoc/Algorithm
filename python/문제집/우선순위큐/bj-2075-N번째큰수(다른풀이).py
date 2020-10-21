import sys
import heapq
input = sys.stdin.readline

'''
내가 푼 첫 번째 풀이보다 약간의 시간차이가 생김
200~300ms 정도 더 빠른 풀이
이유는 arr의 length를 계산하지 않기때문
'''

n = int(input())
arr = []

for num in map(int, input().split()):
    heapq.heappush(arr, num)

for i in range(1, n):
    for num in map(int, input().split()):
        heapq.heappush(arr, num)
        heapq.heappop(arr)

print(heapq.heappop(arr))
