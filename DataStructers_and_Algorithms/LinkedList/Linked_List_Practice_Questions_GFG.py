#Q1 - Print the middle of a linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class NodeOperation:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def CreateSLL(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
        else:
            newNode.next=self.head
            self.head=newNode

    def getLen(self):
        len=0
        node=self.head
        while node is not None:
            len+=1
            node=node.next
        return len
    #Q1.Print the Middle of a given linked list
    def printMiddle(self):
        node=self.head
        if node is not None:
            len=self.getLen()
            temp=node
            mid=len//2
            while mid != 0:
                temp=temp.next
                mid-=1
            print("The middle element is %d"%temp.data)
    #Q4.Delete middle of a linked list
    def DeleteMid(self):
        node=self.head
        if node is not None:
            len=self.getLen()
            if len%2==0:
                delnode=(len//2)+1
                print(delnode)
                index=0
                while index<delnode-2:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next

            else:
                delnode=((len+1)//2)
                print(delnode)
                index=0
                while index<delnode-2:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next

    def removeDup(self):
        tempnode=self.head
        print(tempnode.value)
        visited=set([tempnode.value])
        while tempnode:
            if tempnode.value in visited:
                tempnode.next=tempnode.next.next
            else:
                visited.CreateSLL(tempnode.value)
                tempnode=tempnode.next
        return




createSLL=NodeOperation()
createSLL.CreateSLL(1)
createSLL.CreateSLL(2)
createSLL.CreateSLL(3)
createSLL.CreateSLL(4)
print([node.data for node in createSLL])
createSLL.printMiddle()
#createSLL.DeleteMid()
print([node.data for node in createSLL])
print(createSLL.removeDup())