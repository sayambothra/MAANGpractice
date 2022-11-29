def MNnodes(M,N,ll):
    tempnode=ll.head
    for i in range(1,M):
        tempnode=tempnode.next
    # print(tempnode.data)
    temp=tempnode.next
    #print(temp.data)
    for i in range(N):
        temp=temp.next
    tempnode.next=temp
    #print(tempnode.data)
    tempnode=temp
    return ll
def getNthFromLast(ll,n):
    tempNode=ll.head
    print(tempNode.data)
    lenll=0
    while tempNode is not None:
        lenll+=1
        tempNode=tempNode.next
    print(lenll)
    nthElement=lenll-n
    print(nthElement)
    if lenll < n:
        print("1")
    else:
        temp=ll.head
        for i in range(nthElement-1):
            temp=temp.next
    print(temp.data)

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
            self.head = newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def printList(self):
        tempNode=self.head
        if tempNode is None:
            print("")
        else:
            while tempNode:
                print(tempNode.data,end="->")
                tempNode=tempNode.next
if __name__ == "__main__":
    M=int(input())
    N=int(input())
    t=input().split()
    a=LinkedList()
    for i in t:
        a.append(int(i))
    a.printList()
    MNnodes(M,N,a)
    print("")
    a.printList()
    getNthFromLast(a,2)

