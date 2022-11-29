class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
            newNode.prev=None
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            newNode.next=None
            self.tail=newNode
    def printList(self):
        if self.head is None:
            print("The List is Empty")
        else:
            tempNode=self.head
            while tempNode is not None:
                print(tempNode.data,end=" ")
                # if tempNode.next is None:
                #     print()
                # else:
                #     print("->",end="")
                tempNode=tempNode.next
        #print()
    def reverseLL(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.data,end="")
            if tempNode.prev is None:
                 print("")
            else:
                 print("->", end="")
            tempNode = tempNode.prev
        #print()
if __name__=="__main__":
    t=input().split()
    print(t)
    a=DoublyLinkedList()
    for i in t:
        #print(i)
        a.append(int(i))
    a.printList()
    print()
    a.reverseLL()




