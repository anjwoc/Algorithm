#큐는 BFS와 Flood Fill에서 사용된다.
#BFS와 Flood Fill외 에는 코딩테스트에 안나옴

class Queue:
    def __init__(self):
        self.Queue_item = []

    #Enqueue 기능 구현
    def Enqueue(self, x):
        self.Queue_item.append(x)
        return None

    #Dequeue 기능 구현
    def Dequeue(self):
        if(self.isEmpty() == True):
            print("Queue is empty")
            return False
        result = self.Queue_item[0]
        del (self.Queue_item[0])
        return result
    #isEmpty 기능 구현
    def isEmpty(self):
        return not self.Queue_item

if __name__=="__main__":
    test = Queue()
    print(test.Queue_item)
    test.Enqueue(1)
    print(test.Queue_item)
    print(test.Dequeue())
    test.Enqueue(2)
    test.Enqueue(3)
    test.Enqueue(4)
    test.Enqueue(5)
    print(test.Queue_item)
    print(test.Dequeue())
    print(test.Dequeue())
    print(test.Dequeue())
    print(test.Dequeue())
    print(test.Dequeue())
    print(test.isEmpty())


