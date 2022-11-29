class CQueue:
    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    def isFull(self):
        if self.top+1 ==self.start:
            return True
        elif self.start == 0 and self.top+1 == self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def Enqueue(self,value):
        if self.isFull():
            return "the queue is Full"
        else:
            if self.top+1 == self.maxSize:
                self.top ==0
            else:
                self.top+=1
                if self.start == -1:
                    self.start =0
                self.items[self.top]=value
                return "the element has been inserted successfully"
    def Dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start == self.top:
                self.start = -1
                self.top =-1
            elif self.start+1 == self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start] = None
            return firstElement
    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items[self.start]
    def Delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1




customQueue=CQueue(4)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.Enqueue(1)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
customQueue.Enqueue(4)
customQueue.Enqueue(5)
print(customQueue)
print(customQueue.isFull())
print(customQueue.Dequeue())
print(customQueue)
print(customQueue.peek())


