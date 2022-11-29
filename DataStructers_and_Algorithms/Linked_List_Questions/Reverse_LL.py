class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '-> '.join(values)

    def add(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
            newNode.prev=None
        else:
            newNode.next=None
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
        return self.tail
    def len1(self,ll):
        tempNode=ll.head
        count = 0
        while tempNode is not None:
            count = count + 1
            tempNode=tempNode.next

        return count

    def ReverseLL(self,ll):
        tempNode=ll.tail
        while tempNode:
            print(tempNode.value,end="->")
            tempNode=tempNode.prev



singlyLL=LinkedList()
singlyLL.add(1)
singlyLL.add(2)
singlyLL.add(3)
singlyLL.add(4)
print(singlyLL)
print(singlyLL.ReverseLL(singlyLL))