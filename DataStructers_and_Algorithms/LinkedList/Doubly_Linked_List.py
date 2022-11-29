class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    #Creation of Doubly Linked list  - TC:O(1),SC:O(1)
    def CreateDLL(self,nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "The DLL is created Successfully"
    # insertion in Doubly Linked List - TC:O(n),SC:O(1)
    def InsertDLL(self,nodeValue,location):
        if self.head is None:
            print("the node cannot be inserted")
        else:
            newNode=Node(nodeValue)
            if location == 0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location == 1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location - 1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next =tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
    #Traversal in Doubly linked List - TC:O(n), SC:O(1)
    def TraverseDLL(self):
        if self.head is None:
            print("List is Empty")
        else:
            node=self.head
            while node is not None:
                print(node.value,end=" , ")
                node=node.next
    #Reverse Traversal in Doubly Linked list - TC;O(n),SC:O(1)
    def RTraverseDLL(self):
        if self.head is None:
            print("List is Empty")
        else:
            node = self.tail
            while node is not None:
                print(node.value,end=" , ")
                node = node.prev
    #Searching in Doubly Linked list - TC:O(n),SC:O(1)
    def SearchDLL(self,value):
        if self.head is None:
            print("List is Empty")
        else:
            node=self.head
            while node is not None:
                if node.value==value:
                    print(node.value)
                node=node.next
            return "Element does not exist"
    #Deleting a node in Doubly Linked List - TC:O(n),SC;O(1)
    def DeleteDSLL(self,location):
        if self.head is None:
            print("The List is Empty")
        else:
            if location == 0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                tempNode=self.head
                index=0
                while index < location - 1:
                    tempNode=tempNode.next
                    index+=1
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
            print("the node has been successfully deleted")

    # Deleting Entire Doubly Linked List - TC:O(n),SC:O(1)
    def DeleteCDLL(self):
        if self.head is None:
            print("The List is Empty")
        else:
            tempNode=self.head
            # self.head = None
            # self.tail = None
            while tempNode is not None:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head = None
            self.tail = None
            print("The DLL is deleted")









doublyLL=DoublyLL()
doublyLL.CreateDLL(5)
print([node.value for node in doublyLL])
doublyLL.InsertDLL(1,0)
doublyLL.InsertDLL(3,1)
doublyLL.InsertDLL(2,1)
doublyLL.InsertDLL(4,1)
print([node.value for node in doublyLL])
doublyLL.TraverseDLL()
print()
doublyLL.RTraverseDLL()
print()
print(doublyLL.SearchDLL(6))
doublyLL.DeleteDSLL(0)
print([node.value for node in doublyLL])
doublyLL.DeleteCDLL()
print([node.value for node in doublyLL])