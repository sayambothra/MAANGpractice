def Delzero(head):
    tempNode=head
    pos=list()
    neg=list()
    while tempNode is not None:
        if tempNode.data >=0:
            pos.append(tempNode.data)
        else:
            neg.append(tempNode.data)
        tempNode=tempNode.next
    pSum=sum(pos)
    nSum=sum(neg)
    diff=pSum+nSum
    print(pos)
    res=0
    location = 0
    for i in range(len(pos)):

    print(location)


    print(pSum+nSum)




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
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
            self.tail.next=newNode
            self.tail=newNode
    def printList(self):
        if self.head is None:
            print("")
        else:
            curNode=self.head
            while curNode is not None:
                print(curNode.data,end=" ")
                curNode=curNode.next
            print(' ')

if __name__ == '__main__':
    n=input("number of elements in the list")
    a=LinkedList()
    nodes=list(map(int,input().strip().split()))
    for i in nodes:
        a.append(i)
    a.printList()
    Delzero(a.head)





