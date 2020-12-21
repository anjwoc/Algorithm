import sys
from collections import deque

input = sys.stdin.readline

max_a, max_b, max_c = map(int, input().split())
visited = dict()
ans = set()
ans.add(max_c)
que = deque([(0, 0, max_c)])

def calc(_from, _to, max_value, x):
  if _from + _to > max_value:
    _from = _from + _to - max_value
    _to = max_value
  else:
    _to = _from + _to
    _from = 0
  return _from, _to, x

def check(A, B, C):
  try:
    if visited[(A, B, C)] == 1:
      return False
  except KeyError:
    visited[(A, B, C)] = 1
    if A == 0:
      ans.add(C)
    return True

while que:
  a, b, c = que.popleft()
  # case1 => a->b
  na, nb, nc = calc(a, b, max_b, c)
  if check(na, nb, nc):
    que.append((na, nb, nc))
  
  # case2 => a->c
  na, nc, nb = calc(a, c, max_c, b)
  if check(na, nb, nc):
    que.append((na, nb, nc))
  
  # case3 => b->a
  nb, na, nc = calc(b, a, max_a, c)
  if check(na, nb, nc):
    que.append((na, nb, nc))
  
  # case4 => b->c
  nb, nc, na = calc(b, c, max_c, a)
  if check(na, nb, nc):
    que.append((na, nb, nc))
  
  # case5 => c->a
  nc, na, nb = calc(c, a, max_a, b)
  if check(na, nb, nc):
    que.append((na, nb, nc))

  # case6 => c->b
  nc, nb, na = calc(c, b, max_b, a)
  if check(na, nb, nc):
    que.append((na, nb, nc))

ans = sorted(ans)
for i in ans:
  print(i, end=' ')