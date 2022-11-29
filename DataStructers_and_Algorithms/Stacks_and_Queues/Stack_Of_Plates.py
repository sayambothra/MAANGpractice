class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list1=[]
    def __str__(self):
        values=reversed(self.list1)
        values=[str(x) for x in values]
        return ','.join(values)

    def push(self,item):
        if len(self.list1) > 0 and (len(self.list1[-1])) < self.maxsize:
            self.list1[-1].append(item)
        else:
            self.list1.append([item])

    def pop(self):
        while len(self.list1)  and len(self.list1[-1]) == 0:
            self.list1.pop()

        if len(self.list1) == 0:
            return None
        else:
            return self.list1[-1].pop()

    def pop_at(self,stackNumber):
        if len(self.list1[stackNumber]) > 0:
            return self.list1[stackNumber].pop()
        else:
            return None

custStack=Stack(2)
custStack.push(1)
custStack.push(2)
custStack.push(3)
custStack.push(4)
print(custStack.pop_at(1))
print(custStack.pop_at(1))
print(custStack.pop_at(1))


