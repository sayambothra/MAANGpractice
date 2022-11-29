class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next
class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        return '->'.join(values)

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def push(self,value):  #TC:O(1),SC:O(1)
        newNode=Node(value)
        newNode.next=self.LinkedList.head
        self.LinkedList.head=newNode
    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    def Delete(self):
        self.LinkedList.head=None

CustomStack=Stack()
print(CustomStack.isEmpty())
CustomStack.push(1)
CustomStack.push(2)
CustomStack.push(3)
CustomStack.push(4)
print(CustomStack)
print("-------")
CustomStack.pop()
print(CustomStack)
print(CustomStack.peek())
CustomStack.Delete()
print(CustomStack)
print(CustomStack.isEmpty())

