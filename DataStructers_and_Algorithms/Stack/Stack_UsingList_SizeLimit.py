class Stack1:
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]
    def __str__(self):
        values=reversed(self.list)
        values=[str(x) for x in values]
        return ','.join(values)
    #isEmpty - TC:O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    #isFull() -
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    # Push() Method
    def push(self,value): #TC:amortized O(1)
        if self.isFull():
            return "The Stack is Full"
        self.list.append(value)
        return "the element has been successfully inserted"
    # pop() method - TC:O(1),SC:O(1)
    def pop(self):
        if self.isEmpty():
            return " The Stack is Empty"
        else:
            return self.list.pop()

    # peek() - TC:O(1),SC:O(1)
    def peek(self):
        if self.isEmpty():
            return " the list Empty"
        else:
           return self.list[len(self.list) - 1]

    # delete
    def delete(self):
         self.list = None
CustomStack =Stack1(4)
CustomStack.isEmpty()
CustomStack.isFull()
CustomStack.push(4)
CustomStack.push(3)
CustomStack.push(2)
print(CustomStack)
print(CustomStack.push(1))
print(CustomStack)
print(CustomStack.push(0))
print(CustomStack)