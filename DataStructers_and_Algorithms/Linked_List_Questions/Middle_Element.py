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
        while node is not None:
            yield node
            node=node.next


    def __str__(self):
        values =[str(x.value) for x in self]
        return '-> '.join(values)



    def add(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
        else:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode
        return self.tail

    def len1(self,ll):
        tempNode=ll.head
        count=0
        while tempNode.next is not None:
            count+=1
            tempNode=tempNode.next
        return count

    def MiddleElement(self,ll):
        tempNode=ll.head
        lengthofLinkedList=ll.len1(ll)
        if lengthofLinkedList%2 == 0:
            middleElement=lengthofLinkedList/2
        else:
            middleElement=(lengthofLinkedList+1)/2
        index=0
        while tempNode.next is not None:
            if index == middleElement:
                    return tempNode.value

            index+=1
            tempNode=tempNode.next



SinglyLinkedList=LinkedList()
SinglyLinkedList.add(1)
SinglyLinkedList.add(2)
SinglyLinkedList.add(3)
SinglyLinkedList.add(4)
SinglyLinkedList.add(5)
#SinglyLinkedList.add(6)
print(SinglyLinkedList)
print(SinglyLinkedList.len1(SinglyLinkedList))
print(SinglyLinkedList.MiddleElement(SinglyLinkedList))

