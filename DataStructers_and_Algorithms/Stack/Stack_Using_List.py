#Stack Creation using list
''' -Easy to implement
   -speed problem when it grows
   '''

# Stack using Linked list
''' - fast performance
   - Implementation is not easy
 '''

# Stack Creation Using List
class Stack:
    def __init__(self):
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
    # Push() Method
    def push(self,value): #TC:amortized O(1)
        self.list.append(value)
        return "the element has been successfully inserted"
    #pop() method - TC:O(1),SC:O(1)
    def pop(self):
        if self.isEmpty():
            return " The Stack is Empty"
        else:
            return self.list.pop()
    #peek() - TC:O(1),SC:O(1)
    def peek(self):
        if self.isEmpty():
            return " the list Empty"
        else:
            return self.list[len(self.list)-1]
    #delete
    def delete(self):
        self.list=None

customStack =Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack,end=" ")
print()
print(customStack.pop())
print(customStack, end=" ")
print()
print(customStack.peek())
print(customStack)
customStack.delete()

