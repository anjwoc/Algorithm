#클래스로 구현하는 방법
class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if (self.size() != 0):
            return self.items.pop()
        else:
            return -1
    def isEmpty(self):
        if(len(self.items) == 0):
            return 1
        else: 
            return 0
    def size(self):
        return len(self.items)
    def top(self):
        if(self.size() != 0):
            return self.items[-1]
        else:
            return -1


T = int(input())
stk = stack()
for i in range(T):
    tmp = list(map(str, input().split()))
    if(tmp[0] == "push"):
        stk.push(tmp[1])
    elif(tmp[0] == "pop"):
        print(stk.pop())
    elif(tmp[0] == "size"):
        print(stk.size())
    elif(tmp[0] == "empty"):
        print(stk.isEmpty())
    elif(tmp[0] == "top"):
        print(stk.top())


