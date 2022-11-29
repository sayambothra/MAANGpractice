class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        tempNode=self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next

    def __str__(self):
        values=[str(x.value) for x in self]
        return '->'.join(values)

    def add(self,value):
        newNode=Node(value)
        if self.head is None:
            newNode.next=None
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode

    def len1(self):
        tempNode=self.head
        count=0
        while tempNode:
            count+=1
            tempNode=tempNode.next

        return count

    def Delete(self,value):
        tempNode=self.head
        if self.head.value==value:
            self.head=self.head.next

        else:
            index=0
            while tempNode:
                if tempNode.value == value:
                    location = index
                    print(location)
                index+=1
                tempNode=tempNode.next
            newIndex=0
            curNode=self.head
            while curNode:
                if newIndex == location - 1:
                    curNode.next=curNode.next.next
                curNode=curNode.next
                newIndex=newIndex+1
        return self




singlyLL=LinkedList()
singlyLL.add(1)
singlyLL.add(2)
singlyLL.add(3)
singlyLL.add(4)
singlyLL.add(5)
print(singlyLL)
print(singlyLL.Delete(4))

