#Creation of Linked List- TC:O(1),SC:O(1)
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    # insert in Linked List - TC:O(n),SC:O(1)
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location == 0:
                newNode.next=self.head
                self.head=newNode
            elif location == 1:
                newNode.next= None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
                if tempNode==self.tail:
                    self.tail=newNode
    # Traverse Single linked list
    def traverseSSL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node =self.head
            while node is not None:
                print(node.value)
                node=node.next
    # Search in Linked List - TC:O(n),SC:O(1)
    def SearchSSL(self,value):
        if self.head is None:
            print("The Singly Linked List is Empty")
        else:
            node=self.head
            while node is not None:
                if value==node.value:
                    print(node.value)
                    break
                elif node==self.tail:
                    print("Element does not exist")
                node=node.next
    # Search in Linked List -By Udemy
    def SearchSSLU(self,value):
        if self.head is None:
            print("The Singly Linked List is Empty")
        else:
            node=self.head
            while node is not None:
                if value==node.value:
                   return node.value
                node = node.next
            return  "Element does not exist"
    # Deletion in Singly Linked list- TC:O(n),SC:O(1)
    def deleteNode(self,location):
        if self.head is None:
            print("The SSL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next ==self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while index <location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
    # delete entire singly Linked List - TC:O(1), SC:O(1)
      #1 .set head and tail to none
    def DeleteEntireSSl(self):
        if self.head is None:
            print("The SSL does not exist")
        else:
            self.head=None
            self.tail=None
singlyLinkedList=SlinkedList()
# node1=Node(1)
# node2=Node(2)
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,0)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,2)
# singlyLinkedList.head=node1
# singlyLinkedList.head.next=node2
# singlyLinkedList.tail=node2
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverseSSL()
singlyLinkedList.SearchSSL(5)
print(singlyLinkedList.SearchSSLU(5))
singlyLinkedList.deleteNode(1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.DeleteEntireSSl()
print([node.value for node in singlyLinkedList])


