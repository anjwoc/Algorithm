import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = input().split()
arr.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
ans = []


for password in combinations(arr, n):
    cnt = 0
    for i in password:
        if i in vowel:
            cnt += 1

    if 1 <= cnt <= n-2:
        print(''.join(password))
