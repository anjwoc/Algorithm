import sys
from collections import deque
input = sys.stdin.readline

def primes(n):
  sieve = [True] * n
  m = int(n ** 0.5)

  for i in range(2, m+1):
    if sieve[i] == True:
      for j in range(i+1, n, i):
        sieve[j] = False
  
  return [i for i in range(2, n) if sieve[i]]

prime = primes(10000)
