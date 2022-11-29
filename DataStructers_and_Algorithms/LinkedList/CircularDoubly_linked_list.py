
class Node:
    def __init__(self,value=None):
        self.head=None
        self.tail=None
        self.value=value

class CDoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node == self.tail.next:
                break
    #Creation of Ciruclar Doubly Linked List - TC:O(1),SC:O(1)
    def CreateCDLL(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        newNode.next=newNode
        newNode.prev=newNode
        return"The circular Doubly linked list has been created"
    #Insertion in Circular Doubly Linked list - TC:O(n),SC;O(1)
    def InsertCDLL(self,value,location):
        if self.head is None:
            print("the List is Empty")
        else:
            new1Node = Node(value)
            if location == 0:
                new1Node.next=self.head
                new1Node.prev=self.tail
                self.head.prev=new1Node
                self.head=new1Node
                self.tail.next=new1Node
            elif location == 1:
                new1Node.next=self.head
                new1Node.prev=self.tail
                self.head.prev=new1Node
                self.tail.next=new1Node
                self.tail=new1Node
            else:
                tempNode=self.head
                index=0
                while index < location -1:
                    tempNode=tempNode.next
                    index+=1
                new1Node.next=tempNode.next
                new1Node.prev=tempNode
                new1Node.next.prev = new1Node
                tempNode.next=new1Node

            return "The node has been successfully inserted"
    #Traversal in Circular Doubly Linked List - TC:O(n),SC:O(1)
    def TraverseCDLL(self):
        if self.head is None:
            print("The list is Empty")
        else:
            node=self.head
            while node:
                print(node.value)
                if node == self.head:
                     break
                node = node.next
    #Reverse Traversal in Doubly Linked List - TC:O(n),SC:O(1)
    def RTraversalCDLL(self):
        if self.tail is None:
            print("The list is Empty")
        else:
            node=self.tail
            while node is not None:
                print(node.value)
                node=node.prev
                if node == self.head.prev:
                    break
    #Udemy Solution
    def RRTraversalCDLL(self):
        if self.head is None:
            print("The list is Empty")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    #Searching in Circular Doubly Linked list - TC:O(n),SC:O(1)
    def SearchCDLL(self,value):
        if self.head is None:
            return "The list is Empty"
        else:
            node=self.head
            while node:
                if node.value==value:
                     return node.value
                if node == self.tail:
                    return "The element is not present"
                node = node.next
    #Deletion in Circular Doubly Linked List - TC:O(n),SC:O(1)
    def DeleteCDLL(self,location):
        if self.head is None:
            return "The list is empty"
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head.prev=None
                    self.head=None
                    self.tail=None
                else:
                   # self.tail.next=self.head
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif location == 1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head.prev=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                tempNode=self.head
                index=0
                while index < location - 1:
                    #
                    tempNode=tempNode.next#
                    index+=1
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
    #Deleting Entire Circular Doubly linked list - TC:O(n), SC:O(1)
    def EDeleteCDLL(self):
        if self.head is None:
            print("the list is empty")
        else:
            self.tail.next=None
            node=self.head
            while node:
                node.prev=None
                node=node.next
            self.head=None
            self.tail=None

CircularDLL=CDoublyLL()
CircularDLL.CreateCDLL(5)
print([node.value for node in CircularDLL])
print(CircularDLL.InsertCDLL(3,0))
CircularDLL.InsertCDLL(1,1)
CircularDLL.InsertCDLL(2,2)
CircularDLL.InsertCDLL(4,3)
print([node.value for node in CircularDLL])
CircularDLL.TraverseCDLL()
CircularDLL.RTraversalCDLL()
CircularDLL.RRTraversalCDLL()
print(CircularDLL.SearchCDLL(5))
print([node.value for node in CircularDLL])
CircularDLL.DeleteCDLL(3)
print([node.value for node in CircularDLL])
CircularDLL.EDeleteCDLL()
print([node.value for node in CircularDLL])