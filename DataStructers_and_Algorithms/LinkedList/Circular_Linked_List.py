class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class CircularSSL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            if node.next ==self.head:
                break
            node = node.next


    #Creation of circular Singly lInked List
    def CreateCSLL(self,value):
        node=Node(value)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been ceated"

    #Insertion in Circular Singly Linked list - TC:O(n),SC:O(1)
    def InserCSLL(self,value,location):
        if self.head is None:
            node = Node(value)
            node.next = node
            self.head = node
            self.tail = node
            #return "The list is Empty"
        else:
            newNode=Node(value)
            if location == 0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location == 1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index <  location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            return "The node has been successfully inserted"
    #Traverse in Circular Singly Linked List - TC:O(n),SC:O(1)
    def TraverseCSLL(self):
        if self.head is None:
            return "List is Empty"
        else:
            node=self.head
            while node:
                print(node.value)
                node=node.next
                if node== self.tail.next:
                    break
    #Searching in Circular Singly Linked List - TC:O(n), SC:O(1)
    def SearchCSLL(self,value=None):
        if self.head is None:
            return "List is Empty and value does not exist"
        else:
            node=self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node=node.next
                if node==self.tail.next:
                    return "Element not found"

    # Delete a node from Circular Singly Linked list - TC:O(n),SC:O(1)
    def deleteNode(self,location):
        if self.head is None:
            print("The list is empty")
        else:
            if location == 0:
                if self.tail == self.head:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            if location == 1:
                if self.tail == self.head:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next

    # Delete entire CSLL - TC:O(1),SC:O(1)
    def deleteECSLL(self):
        self.head=None
        self.tail.next=None
        self.tail = None





CircularSinglyLL=CircularSSL()
CircularSinglyLL.CreateCSLL(1)
print([node.value for node in CircularSinglyLL])
CircularSinglyLL.InserCSLL(0,0)
CircularSinglyLL.InserCSLL(4,1)
CircularSinglyLL.InserCSLL(5,1)
CircularSinglyLL.InserCSLL(2,1)
print([node.value for node in CircularSinglyLL])
CircularSinglyLL.TraverseCSLL()
print(CircularSinglyLL.SearchCSLL(6))
print([node.value for node in CircularSinglyLL])
CircularSinglyLL.deleteNode(2)
print([node.value for node in CircularSinglyLL])
CircularSinglyLL.deleteECSLL()
print([node.value for node in CircularSinglyLL])

