class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def __str__(self):
        values=[str(x.value) for x in self]
        return '-> '.join(values)

    def push(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            newNode.next=None
            self.tail=newNode
        else:
            if newNode.value <= self.head.value:
                newNode.next = self.head
                self.head=newNode
            else:
                self.tail.next=newNode
                newNode.next=None
                self.tail=newNode
    def pop(self):
        if self.head is None:
            return "The List is Empty"
        else:
            newNode=self.head.value
            self.head=self.head.next
            return newNode


singlyLL=LinkedList()
singlyLL.push(5)
singlyLL.push(6)
print(singlyLL.pop())
singlyLL.push(3)
print(singlyLL)
singlyLL.push(7)
print(singlyLL)
print(singlyLL.pop())

