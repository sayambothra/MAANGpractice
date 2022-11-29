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

    def AddNum(self,llA,llB):
        if (llA.head and llB.head) is None:
            return
        tempNodeA=llA.head
        num1=0
        while tempNodeA:
            num1=(num1*10)+tempNodeA.value
            tempNodeA=tempNodeA.next
        tempNodeB = llB.head
        num2 = 0
        while tempNodeB:
            num2 = (num2 * 10) + tempNodeB.value
            tempNodeB = tempNodeB.next

        return num1+num2


singlyLLA=LinkedList()
singlyLLB=LinkedList()
singlyLLA.add(5)
singlyLLA.add(6)
singlyLLA.add(3)
singlyLLB.add(8)
singlyLLB.add(4)
singlyLLB.add(2)

print(singlyLLA.AddNum(singlyLLA,singlyLLB))

