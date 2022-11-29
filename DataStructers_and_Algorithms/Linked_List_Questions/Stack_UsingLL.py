class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
     def __init__(self):
         self.LinkedList=linkedList()

     def __str__(self):
         values=[str(x.value) for x in self.LinkedList ]
         return '->'.join(values)

     def push(self,value):
         newNode=Node(value)
         if self.LinkedList.head is None:
             self.LinkedList.head=newNode
             self.LinkedList.tail=newNode
         else:
             newNode.next=self.LinkedList.head
             self.LinkedList.head=newNode


     def pop(self):
         if self.LinkedList.head is None:
             return " List is Empty"
         else:
             tempNode=self.LinkedList.head
             self.LinkedList.head=self.LinkedList.head.next
             return tempNode.value

     def peek(self):
         if self.LinkedList.head is None:
             return " List is Empty"
         else:
             tempNode = self.LinkedList.head
             return tempNode.value




custStack=Stack()
custStack.push(1)
custStack.push(2)
custStack.push(3)
print(custStack)
print(custStack.pop())
print(custStack)
