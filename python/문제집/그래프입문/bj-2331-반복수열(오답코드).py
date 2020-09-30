import sys
input = sys.stdin.readline

def get_value(value):
  ret = 0
  for i in value:
    ret += int(i)**int(p)
  return str(ret)


a, p = input().split()
num = 0

for i in a:
  num += int(i)**int(p)
num = str(num)
dic = dict()
dic = {a: True, num: True}
arr = [a, num]

while True:
  data = get_value(str(arr[-1]))
  if data in dic:
    idx = arr.index(data)
    break
  arr.append(data)
  dic[data] = True
  

