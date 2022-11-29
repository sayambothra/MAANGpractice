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
        return '->'.join(values)

    def push(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            newNode.next=None
        else:
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode

    def len1(self,ll):
        tempNode=ll.head
        count=0
        while tempNode:
            count+=1
            tempNode=tempNode.next
        return count

    def NumberOf0(self,ll):
        tempNode=ll.head
        print(tempNode.value)
        count0=0
        count1=0
        count2=0
        while tempNode:
            if tempNode.value == 0:
                count0+=1
                tempNode=tempNode.next
            elif tempNode.value == 1:
                count1 += 1
                tempNode = tempNode.next
            elif tempNode.value == 2:
                count2 += 1
                tempNode = tempNode.next
        return count0,count1,count2




    def Sort0_1_2(self,ll):
        NumberOfZero=self.NumberOf0(ll)[0]
        NumberOfOne=self.NumberOf0(ll)[1]
        NumberOfTwo=self.NumberOf0(ll)[2]
        # print(NumberOfZero)
        # print(NumberOfOne)
        # print(NumberOfTwo)
        tempNode=ll.head
        index=0
        while tempNode:
            if index < NumberOfZero:
                print("When index is less than 0",tempNode.value,index)
                tempNode.value=0
                tempNode=tempNode.next
                index+=1
                #print(index)
            elif index >= NumberOfZero and index < NumberOfOne:
                print("When value is equal to 1",tempNode.value,index)
                tempNode.value=1
                tempNode=tempNode.next
                index+=1
                #print(index)
            elif index >= NumberOfOne and index < NumberOfTwo:
                print("When index is equal to 2",tempNode.value,index)
                tempNode.value=2
                tempNode=tempNode.next
                index+=1
                #print(index)






singlyLL=LinkedList()
singlyLL.push(1)
singlyLL.push(1)
singlyLL.push(2)
singlyLL.push(0)
singlyLL.push(2)
singlyLL.push(0)
singlyLL.push(1)
print(singlyLL)
print(singlyLL.len1(singlyLL))
print(singlyLL.NumberOf0(singlyLL))
#print(singlyLL.Sort0_1_2(singlyLL))
print(singlyLL)
# print(singlyLL.NumberOf1(singlyLL))
# print(singlyLL.NumberOf2(singlyLL))



