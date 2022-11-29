#Creation of binary Tree - TC:O(1),SC:O(n)
class BinaryTree:
    def __init__(self,size):
        self.customList= size * [None]
        self.lastUsedIndex = 0
        self.maxSize=size

# Insertion of a node in a binary Tree -  TC:O(1),SC:O(1)
    def insertNode(self,value):
        self.value=value
        if self.lastUsedIndex+1==self.maxSize:
            return " the Binary Tree is full"
        self.lastUsedIndex += 1
        self.customList[self.lastUsedIndex] = self.value
        return "The value has been successfully inserted"
#Searching of a node in a Binary Tree -  TC:O(n),SC:O(1)
    def SearchNode(self,nvalue):
        for i in range(len(self.customList)):
            if self.customList[i] == nvalue:
                return "Success"
        return "Not Found"
#PreOrder Traversal in Binary Tree - TC:O(n),SC:O(n)
    def PreOrder(self,index):
        if index > self.lastUsedIndex:
           return
        print(self.customList[index])
        self.PreOrder(index*2)
        self.PreOrder(index*2 + 1)
#inOrder Traversal in Binary Tree - TC:O(n),SC:O(n)
    def inOrder(self,index):
        if index >self.lastUsedIndex:
            return
        self.inOrder(index*2)
        print(self.customList[index])
        self.inOrder(index*2 + 1)
#postOrder Traversal in Binary Tree - TC:O(n),SC:O(n)
    def postOrder(self,index):
        if index >self.lastUsedIndex:
            return
        self.postOrder(index*2)
        self.postOrder(index*2 + 1)
        print(self.customList[index])

#LevelOrder Traversal in Binary Tree - TC:O(n),SC:O(1)
    def levelOrder(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])

# delete a node from Binary Tree - TC:O(n),SC:O(1)
    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "The tree is Empty"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex-=1
                return "the node has been deleted"

#delete Entire Binary Tree - TC:O(1),SC:O(1)
    def delete(self):
        self.customList[self.lastUsedIndex] =None
newBT=BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.insertNode("alcoholic")
newBT.insertNode("non-alcoholic")
print(newBT.SearchNode("Hot"))
newBT.PreOrder(1)
newBT.inOrder(1)
newBT.postOrder(1)
newBT.levelOrder(1)
print(newBT.deleteNode("Tea"))
newBT.levelOrder(1)
newBT.delete()
newBT.levelOrder(1)
