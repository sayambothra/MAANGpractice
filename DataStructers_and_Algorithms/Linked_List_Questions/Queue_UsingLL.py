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

class Queue:
     def __init__(self):
         self.LinkedList=linkedList()

     def __str__(self):
         values=[str(x.value) for x in self.LinkedList ]
         return '->'.join(values)

     def Enqueue(self,value):
         newNode=Node(value)
         if self.LinkedList.head is None:
             self.LinkedList.head=newNode
             self.LinkedList.tail=newNode
         else:
             self.LinkedList.tail.next=newNode
             self.LinkedList.tail=newNode


     def Dequeue(self):
         if self.LinkedList.head is None:
             return " List is Empty"
         else:
             tempNode=self.LinkedList.head
             self.LinkedList.head=self.LinkedList.head.next
             return tempNode.value



custQueue=Queue()
custQueue.Enqueue(1)
custQueue.Enqueue(2)
custQueue.Enqueue(3)
print(custQueue)
print(custQueue.Dequeue())
print(custQueue)
