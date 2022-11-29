class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

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
        values = [str(x.value) for x in self]
        return '-> '.join(values)

    def add(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
            newNode.prev=None
        else:
            newNode.next=None
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail=newNode
        return self.tail
    def len1(self,ll):
        tempNode=ll.head
        count = 0
        while tempNode is not None:
            count = count + 1
            tempNode=tempNode.next

        return count

    def Merge(self,llA,llB):
        tempNode=llA.tail
        tempNode.next=llB.head
        return llA

    def MergeSort(self,llA,llB):
        tempNode=self.Merge(llA,llB)
        #print(tempNode.head.value)
        curNode = tempNode.head
        print(curNode.value)
        while curNode is not None:
            newNode = curNode
            print(newNode.value,end=",")
            checkNode = newNode.next
            print(checkNode.value)
            while checkNode is not None:
                if newNode.value > checkNode.value:
                    newNode.value, checkNode.value = checkNode.value, newNode.value
                    checkNode = checkNode.next
                else:
                    checkNode=checkNode.next
            curNode = curNode.next


singlyLLA=LinkedList()
singlyLLB=LinkedList()
singlyLLA.add(5)
singlyLLA.add(10)
singlyLLA.add(15)
singlyLLB.add(2)
singlyLLB.add(3)
singlyLLB.add(20)
print(singlyLLA.MergeSort(singlyLLA,singlyLLB))
print([node.value for node in singlyLLA])