import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]

print(pos)
for i in sorted(pos, key=lambda x: (x[0], x[1])):
    print(*i)
