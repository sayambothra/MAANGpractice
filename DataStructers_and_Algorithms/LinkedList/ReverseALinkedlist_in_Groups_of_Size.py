def reversebySize(ll,size):
    lenLinkedList=len(ll)
    count=1
    list1=list()
    while count <= size:
        tempNode=ll.head







class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
    def printList(self):
        if self.head is None:
            print(" ")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.data,end=" ")
                # if tempNode.next is None:
                #     print(" ",end=" ")
                # else:
                #     print("->",end=" ")
                tempNode=tempNode.next
    def __len__(self):
        tempNode=self.head
        res=0
        while tempNode:
            res+=1
            tempNode=tempNode.next
        return res

if __name__=="__main__":
    n=int(input("number of elements in the list"))
    size=int(input())
    a=LinkedList()
    nodes=list(map(int,input().strip().split()))
    for x in nodes:
        a.append(x)
    a.printList()
    print()
    reversebySize(a,size)

    a.printList()
