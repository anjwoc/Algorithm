import sys
input = lambda: sys.stdin.readline().strip()

# 부모 노드를 찾는 함수
def getParent(arr, n):
  if arr[n] == n:
    return n
  return getParent(arr, arr[n])

# 두 부모 노드를 합치는 함수
def unionParent(arr, n1, n2):
  a = getParent(arr, n1)
  b = getParent(arr, n2)
  if a < b:
    arr[b] = a
  else:
    arr[a] = b

# 같은 부모를 가지는지 확인
def findParent(arr, n1, n2):
  a = getParent(arr, n1)
  b = getParent(arr, n2)
  if a==b: return 1
  else: return 0

edges = []
parent = {}
V, E = map(int, input().split())
for _ in range(E):
  edges.append(list(map(int, input().split())))

# 부모노드 dict를 초기화
# 모든 노드가 자기 자신을 부모노드로 저장
for i in range(V):
  parent[i+1] = i+1

# 가중치의 오름차순으로 간선을 정렬
edges.sort(key=lambda cost: cost[2])

MST = []
# Kruskal's Algorithm
for e in edges:
  v, u, w = e
  # 두 노드의 부모노드가 같은지 비교
  if findParent(parent, v, u) == 0:
    # 부모노드가 같지 않다면 두 노드를 연결하고, 아니면 더 낮은 숫자를 가진 노드로 부모노드를 변경
    unionParent(parent, v, u)
    # 최소 비용 신장트리의 결과 리스트에 현재 간선의 정보 추가
    MST.append(e)

print(sum([w for v, u, w in MST]))


