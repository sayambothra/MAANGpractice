from random import randint
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
    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self

    def removeDups(self,ll):
        if ll.head is None:
            return
        else:
            tempNode=ll.head
            visited=set([tempNode.value])
            while tempNode.next is not None:
                if tempNode.next.value in visited:
                    tempNode.next=tempNode.next.next
                else:
                    visited.add(tempNode.next.value)
                    tempNode=tempNode.next

            return visited
    def nThToLast(self,location,ll):
        if ll.head is None:
            return
        else:
            tempNode=ll.head
            index=0
            position=ll.len1(ll)-location
            while tempNode.next is not None:
                if index == position:
                    return tempNode.next.value
                tempNode = tempNode.next
                index=index+1
    def Nlast(self,ll,location):
        if ll.head is None:
            return
        else:
            tempNode=ll.tail
            index = 0
            while tempNode.prev is not None:
                if index == location-1:
                    return tempNode.value
                tempNode=tempNode.prev
                index= index+1

    def Partition(self,ll,value):
            curNode=ll.head
            ll.tail = curNode
            while curNode:
                nextNode=curNode.next
                curNode.next=None
                if curNode.value < value:
                    print(curNode.value)
                    curNode.next=ll.head
                    ll.head=curNode
                    #tempNode = tempNode.next
                else:
                    print(curNode.value)
                    self.tail.next=curNode
                    self.tail=curNode
                curNode=nextNode
            if ll.tail.next is not None:
                ll.tail.next=None


    '''
    PseudoCode for Intersection :
    Step 1 - Check if the tail node has same reference
    Step 2 - find the length of both the linked lists
    Step 3 - find the differnce in the length of longer and shorter linked list if they are not of same size
    Step 4 - Loop till extra elements of the longer Linked list
    Step 5  - Loop till Shorter ll.node is not Longer ll.node
    Step 6 - return longer ll.node when they are equal
    
    '''
    def Intersection(self,llA,llB):
        if llA.tail is not llB.tail:
            return False

        lenA=llA.len1(llA)
        lenB=llB.len1(llB)

        shorter = llA if lenA < lenB else llB
        longer = llB if lenA < lenB else llA
        diff=llA.len1(longer)-llA.len1(shorter)
        shorterNode=shorter.head
        longerNode=longer.head
        for i in range(diff):
            longerNode=longerNode.next
        while shorterNode is not longerNode:
            shorterNode=shorterNode.next
            longerNode=longerNode.next

        return longerNode.value

    def addSameNode(self,llA,llB,value):
        tempNode=Node(value)
        llA.tail.next=tempNode
        llA.tail=tempNode
        llB.tail.next = tempNode
        llB.tail = tempNode

    def SumLists(self,ll1,ll2):
        tempNode1=ll1.tail
        tempNode2=ll2.tail
        numLL1=0
        numLL2=0
        while tempNode1 is not None:
            numLL1=(numLL1*10)+tempNode1.value
            tempNode1=tempNode1.prev
        while tempNode2 is not None:
            numLL2 = (numLL2 * 10) + tempNode2.value
            tempNode2=tempNode2.prev

        return numLL1+numLL2

    def MiddleElement(self, ll):
        tempNode = ll.head
        lengthofLinkedList = ll.len1(ll)
        middleElement = lengthofLinkedList / 2
        index = 0
        while tempNode.next is not None:
            if index == middleElement:
                if lengthofLinkedList % 2 == 0:
                    return tempNode.value
                else:
                    return tempNode.next.value
            index += 1
            tempNode = tempNode.next






SinglyLinkedList= LinkedList()
# singlyLinkedList1=LinkedList()
# singlyLinkedList2=LinkedList()
SinglyLinkedList.add(1)
SinglyLinkedList.add(2)
SinglyLinkedList.add(3)
SinglyLinkedList.add(4)
SinglyLinkedList.add(5)
SinglyLinkedList.add(6)
print(SinglyLinkedList)
print(SinglyLinkedList.len1(SinglyLinkedList))
print(SinglyLinkedList.MiddleElement(SinglyLinkedList))

# singlyLinkedList.add(11)
# singlyLinkedList.add(3)
# singlyLinkedList.add(9)
# singlyLinkedList.add(10)
# singlyLinkedList.add(15)
# singlyLinkedList1.add(7)
# singlyLinkedList1.add(1)
# singlyLinkedList1.add(6)
#
# singlyLinkedList2.add(5)
# singlyLinkedList2.add(9)
# singlyLinkedList2.add(2)
# singlyLinkedList.addSameNode(singlyLinkedList2,singlyLinkedList1,14)
# singlyLinkedList.addSameNode(singlyLinkedList2,singlyLinkedList1,10)
# singlyLinkedList.addSameNode(singlyLinkedList2,singlyLinkedList1,15)
#
#
# print(singlyLinkedList)
# print(singlyLinkedList1)
# print(singlyLinkedList2)
#print(singlyLinkedList.removeDups(singlyLinkedList))
#print(singlyLinkedList.nThToLast(2,singlyLinkedList))
#print(singlyLinkedList.Nlast(singlyLinkedList,2))
#print(singlyLinkedList.Partition(singlyLinkedList,10))
#print(singlyLinkedList)
#print(singlyLinkedList1.SumLists(singlyLinkedList1,singlyLinkedList2))
# print(singlyLinkedList.Intersection(singlyLinkedList1,singlyLinkedList2))




