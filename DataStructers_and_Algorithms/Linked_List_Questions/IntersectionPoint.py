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
        values=[str(x.values) for x in self]
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

    def Intersection(self,llA,llB):
        if llA.tail is not llB.tail:
            return
        lenA=llA.len1(llA)
        lenB=llB.len1(llB)

        shorter = llA if lenA < lenB else llB
        longer = llB if lenA < lenB else llA

        diff =llA.len1(longer) - llA.len1(shorter)

        shorterNode=shorter.head
        longerNode=longer.head
        for i in range(diff):
            longerNode=longerNode.next

        while shorterNode is not longerNode:
            shorterNode=shorterNode.next
            longerNode=longerNode.next

        return longerNode.value

    def addSameNode(self,llA,llB,value):
        newNode=Node(value)
        llA.tail.next=newNode
        llA.tail=newNode
        llB.tail.next=newNode
        llB.tail=newNode

singlyLLA=LinkedList()
singlyLLB=LinkedList()
singlyLLA.add(1)
singlyLLA.add(2)
singlyLLA.add(3)
singlyLLB.add(4)
singlyLLB.add(5)
singlyLLB.add(6)
singlyLLA.addSameNode(singlyLLA,singlyLLB,7)
singlyLLB.addSameNode(singlyLLA,singlyLLB,8)
print(singlyLLA.Intersection(singlyLLA,singlyLLB))

