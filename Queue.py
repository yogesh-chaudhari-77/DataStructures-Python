class Queue :
    list = list()

    def __init__(self):
        self.list = []

    def enqueue(self, element):
        self.list.append(element)

    def enqueueAll(self, elements : list):
        for i in range(len(elements)) :
            self.enqueue(elements[i])

    def dequeue(self):
        return self.list.pop(0)

    def printQueue(self):
        print(self.list)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.printQueue()
print(queue.dequeue())
print(queue.dequeue())
queue.enqueueAll([4,5,6,7])
queue.printQueue()