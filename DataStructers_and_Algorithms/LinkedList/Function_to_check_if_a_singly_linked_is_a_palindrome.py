class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    list1=list()
    def __init__(self):
        self.head=None
        self.tail=None
    def appendNode(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def printList(self):
        list1=list()
        if self.head is None:
            print("List is Empty")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.data,end=" ")
                list1.append(tempNode.data)
                tempNode = tempNode.next
        return list1






    def push(self,value):
        self.list1.append(value)
    def pop(self):
        self.list1.reverse()
        ele=self.list1.pop()
        return ele
if __name__=="__main__":
    t=input().split()
    print(len(t))
    a=LinkedList()
    for i in t:
        a.appendNode(i)
        a.push(i)
    for i in range(len(t)):
        print(a.pop())

    # d=a.printList()
    # print(d)
    # dr=d[::-1]
    # print(dr)
    # if dr == d:
    #     print("True")
    # else:
    #     print("false")





