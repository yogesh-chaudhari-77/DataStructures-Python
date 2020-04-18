class Stack:
    list = list()

    def __init__(self):
        print("Stack has been generated")

    def pushAll(self, elements:list):
        for i in range(len(elements)):
            self.list.append(elements[i])

    def push(self, element):
        if self.list.append(element) == True:
            return True

    def pop(self):
        # -1 means the element at the end
        return self.list.pop(-1)

    def printStack(self):
        print(self.list)

    def getTop(self):
        return self.list[-1]

newStack = Stack()
print(newStack.push(1))
print(newStack.push(2))
print(newStack.push(3))
print(newStack.pop())
print(newStack.printStack())
print(newStack.getTop())
print(newStack.pushAll([3,4,5,6,7]))
print(newStack.printStack())