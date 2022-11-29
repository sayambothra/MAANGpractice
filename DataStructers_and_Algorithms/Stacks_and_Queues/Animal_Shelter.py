class Queue:
    def __init__(self):
        self.animals=[]

    def __str__(self):
        values=[str(x) for x in self.animals]
        return ','.join(values)

    def Enqueue(self,value):
        self.animals.append(value)

    def DequeueAny(self):
        return self.animals.pop(0)

    def DequeueCat(self):
        for i in range(len(self.animals)-1,-1,-1):
            if self.animals[i] == "Cat":
                return i


    def DequeueDog(self):
        for i in range(len(self.animals)-1,-1,-1):
            if self.animals[i] == "Dog":
                return i


custQueue = Queue()
custQueue.Enqueue("Cat")
custQueue.Enqueue("Dog")
custQueue.Enqueue("Cat")
custQueue.Enqueue("Cat")
custQueue.Enqueue("Dog")
print(custQueue)
#print(custQueue.DequeueAny())
print(custQueue.DequeueCat())
print(custQueue)
print(custQueue.DequeueDog())


