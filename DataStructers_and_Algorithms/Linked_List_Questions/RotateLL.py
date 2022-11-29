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

    def len1(self,ll):
        tempNode=ll.head
        count=0
        while tempNode:
            count+=1
            tempNode=tempNode.next
        return count

    def add(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next =None
        else:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode

    def Rotate(self,ll,k):
        tempNode=ll.head
        index=0
        while index < k-1:
            tempNode=tempNode.next
            index+=1
        ll.tail.next=self.head
        curNode=tempNode.next
        #print(curNode.next.next.value)
        tempNode.next =None
        #print(tempNode.value)

        #print(ll.tail.next.value)
        #return self


        # print(ll.head.value)
        # print(curNode.value)
        curNode1=curNode
        # # print(curNode1.next.value)
        while curNode1 is not None:
             print(curNode1.value,end="->")
             curNode1=curNode1.next





singlyLL=LinkedList()
singlyLL.add(10)
singlyLL.add(20)
singlyLL.add(30)
singlyLL.add(40)
singlyLL.add(50)
singlyLL.add(60)
print(singlyLL)
singlyLL.Rotate(singlyLL,4)
# print([node.value for node in singlyLL])
