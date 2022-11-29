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
            print("The List is Empty")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.data,end="")
                if tempNode.next is None:
                    print(end="")
                else:
                    print("->",end="")
                tempNode=tempNode.next
            print("")
    def DeleteLL(self,location):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location ==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    tempNode=self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode=tempNode.next
                    tempNode.next=None
                    self.tail=tempNode
            else:
                node=self.head
                index=0
                while index < location-1:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next


if __name__ == "__main__":
    n=input().split()
    a=LinkedList()
    for i in n:
        a.append(int(i))
    a.printList()
    a.DeleteLL(1)
    a.printList()

