#Creation of a BST -  TC:O(1),SC:O(1)
import Queue_UsingLL_forTree as Queue
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
#Inserting a node in BST - TC:O(n),SC:O(1)
def insertNode(rootNode,nodeval):
    if rootNode.data  == None:
            rootNode.data=nodeval
    elif nodeval<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeval)
        else:
             insertNode(rootNode.leftChild,nodeval)
    else:
         if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeval)
         else:
              insertNode(rootNode.rightChild,nodeval)
    return "the node has been inserted"
#Traversal in BST
def preOrder(rootNode): #TC:O(n),SC:O(n)
    if rootNode.data is None:
        return
    else:
        print(rootNode.data)
        preOrder(rootNode.leftChild)
        preOrder(rootNode.rightChild)
def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)
def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)

def LevelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue =Queue.Queue()
        customQueue.Enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.Dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.Enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.Enqueue((root.value.rightChild))

#Searching in BST - TC:O(logN),SC:O(logN)
def SearchBST(rootNode,nodeval):

    if rootNode.data == nodeval:
        return "the value is found"
    elif nodeval < rootNode.data:
        if rootNode.leftChild.data == nodeval:
            return "The value is found"
        else:
            SearchBST(rootNode.leftChild,nodeval)
    else:
        if rootNode.rightChild.data == nodeval:
            return "The value is found"
        else:
            SearchBST(rootNode.rightChild,nodeval)
    return "The value does not Exist"


#delete a node from BST - TC:O(logN),SC:O(logN)
def minValue(rootNode):
    curNode=rootNode
    while (curNode.leftChild is not None):
        curNode=curNode.leftChild
    return curNode

def DeleteNode(rootNode,nodeVal):
    if rootNode is None:
        return
    if nodeVal<rootNode.data:
        rootNode.leftChild=DeleteNode(rootNode.leftChild,nodeVal)
    elif nodeVal>rootNode.data:
        rootNode.rightChild=DeleteNode(rootNode.rightChild,nodeVal)
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        if rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp

        temp=minValue(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=DeleteNode(rootNode.rightChild,temp.data)
    return rootNode

#Delete Entire BST -  TC:O(1),SC:O(1)
def DeleteEBST(rootNode):
    rootNode.data=None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return " The BST is Empyt"



newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
#print(newBST)
LevelOrder(newBST)
#print(SearchBST(newBST,400))
print(DeleteNode(newBST,70))
LevelOrder(newBST)

