#Create a Queue Using Linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __str__(self):
        return str(self.value)
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode=curNode.next
class Queue:
    def __init__(self):
        self.LinkedList=linkedList()

    def __str__(self):
        values=[str(x) for x in self.LinkedList]
        return '->'.join(values)
    def Enqueue(self,value): #TC:O(1),SC:O(1)
        newNode=Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head=newNode
            self.LinkedList.tail=newNode
        else:
            self.LinkedList.tail.next=newNode
            self.LinkedList.tail=newNode
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    def Dequeue(self):
        if self.LinkedList.head is None:
            return "The Queue is Empty"
        else:
            tempNode=self.LinkedList.head
            if self.LinkedList.head ==  self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            self.LinkedList.head=self.LinkedList.head.next
            return tempNode
    def peek(self):
        if self.LinkedList.head is None:
            return "The Queue is Empty"
        else:
            return self.LinkedList.head.value
    def Delete(self):
        self.LinkedList.head=None
        self.LinkedList.tail=None


CustomQueue=Queue()
CustomQueue.Enqueue(1)
CustomQueue.Enqueue(2)
CustomQueue.Enqueue(3)
print(CustomQueue)
print(CustomQueue.Dequeue())
print(CustomQueue)
print(CustomQueue.peek())




