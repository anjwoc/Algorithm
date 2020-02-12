class DisjointSet:
  def __init__(self, n):
    self.parent = {}
    self.rank = {}
    for i in range(n):
      self.parent[i] = i
      self.rank[i] = 0

  def find(self, v):
    if self.parent[v] != v:
      self.parent[v] = self.find(self.parent[v])
    return self.parent[v]

  def union(self, root1, root2):
    # 연결 정보를 갱신할 때는 작은 값을 기준으로 갱신
    if self.rank[root1] > self.rank[root2]:
      self.parent[root2] = root1
    else:
      self.parent[root1] = root2
      # self.rank[root2]가 self.rank[root1]보다 크다고 봤으므로 두 값이 같은 경우, self.rank[root2]의 값을 1 올려준다.
      if self.rank[root1] == self.rank[root2]:
        self.rank[root2] += 1


def kruskal(n, info):
  # n은 vertex의 개수
  # info는 vetex간 연결 정보와 link의 weight
  minimum_weight = 0
  disjointset = DisjointSet(n)
  result = []
  for data in sorted(info, key=lambda cost: cost[2]):
    v, u, weight = data
    root1 = disjointset.find(v)
    root2 = disjointset.find(u)
    # root1과 root2가 같은데 연결을 하면 사이클이 생김
    if root1 != root2:
      disjointset.union(root1, root2)
      result.append(data)
      minimum_weight += data[2]

  return result, minimum_weight




print(kruskal(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))

