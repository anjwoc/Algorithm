import sys
from itertools import combinations
input = sys.stdin.readline

def check(char):
  global alphas
  cnt = 0
  for i in char:
    if i in alphas:
      cnt += 1
  
  if 1<=cnt<=L-2:
    return True
  return False

L, C = map(int, input().split())
arr = sorted(input().split())
alphas = ['a', 'e', 'i', 'o', 'u']

lst = combinations(arr, L)

for char in combinations(arr, L):
  if check(char):
    print(''.join(char))
