class Stack:
    def __init__(self):
        self.list1=[]

    def __len__(self):
        return len(self.list1)

    def __str__(self):
        values=[str(x) for x in self]
        return ', '.join(values)

    def push(self,value):
        self.list1.append(value)

    def pop(self):
        return self.list1.pop()

class Queue:
        def __init__(self):
            self.inStack=Stack()
            self.outStack=Stack()

        def enqueue(self,item):
            self.inStack.push(item)

        def Dequeue(self):
            while len(self.inStack):
                self.outStack.push(self.inStack.pop())
            result =self.outStack.pop()
            while len(self.outStack):
                self.inStack.push(self.outStack.pop())
            return result

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue.Dequeue())
custQueue.enqueue(4)
print(custQueue.Dequeue())
