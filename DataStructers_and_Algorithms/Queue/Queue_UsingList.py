#Creating Queue
class Queue:
    def __init__(self):
        self.items=[]
    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def Enqueue(self,value):
        self.items.append(value)
        return "the Element has been Inserted"
    def Dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items[0]
    def delete(self):
        self.items=None

customQueue=Queue()
print(customQueue.isEmpty())
customQueue.Enqueue(1)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
print(customQueue)
customQueue.Dequeue()
print(customQueue)
print(customQueue.peek())

