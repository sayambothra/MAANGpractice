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

    def Swap(self,llA):
        if llA.head is None:
            return
        tempNode=llA.head
        while (tempNode and tempNode.next):
            tempNode.value,tempNode.next.value=tempNode.next.value,tempNode.value
            tempNode=tempNode.next.next


singlyLLA=LinkedList()
singlyLLA.add(1)
singlyLLA.add(2)
singlyLLA.add(3)
singlyLLA.add(4)
singlyLLA.add(5)
print(singlyLLA)
singlyLLA.Swap(singlyLLA)
print([node.value for node in singlyLLA])