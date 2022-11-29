class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def appendNode(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def printList(self):
        tempNode=self.head
        if tempNode is None:
            print("The List is Empty")
        else:
            while tempNode:
                print(tempNode.data,end=" ")
                tempNode=tempNode.next
    def llList(self):
        list1=0
        if self.head is None:
            return
        else:
            node=self.head
            while node:
                list1=list1*10+node.data
                node=node.next
            return list1
    def DelLL(self):
        self.head=None
        self.tail=None
if __name__ =="__main__":
    t=input().split()
    a=LinkedList()
    for i in t:
        a.appendNode(int(i))
    a.printList()
    print()
    llLIST=a.llList()
    a.DelLL()
    add1=llLIST+1
    res=[int(x) for x in str(add1)]
    for i in res:
        a.appendNode(int(i))
    a.printList()
    #print(llLIST)


