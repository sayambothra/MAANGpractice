import Queue_UsingLL_forTree as queue
class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1



def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue=queue.Queue()
    customQueue.Enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root=customQueue.Dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            customQueue.Enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.Enqueue(root.value.rightChild)

def SearchAVL(rootNode,nodeval):
    if rootNode.data==nodeval:
        return "Element is found"
    elif rootNode.data < nodeval:
        if rootNode.rightChild == nodeval:
            return "Element is found"
        else:
            SearchAVL(rootNode.rightChild,nodeval)
    else:
        if rootNode.leftChild  == nodeval:
            return"Element found"
        else:
            SearchAVL(rootNode.leftChild,nodeval)
#Insert a node in AVL TREE  -

#helper function to getHeight
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

#RightRotate - TC:O(1),SC:O(1)
def rightRotate(disbalancedNode):
    newRoot=disbalancedNode.leftChild
    disbalancedNode.leftChild=disbalancedNode.leftChild.rightChild
    newRoot.rightChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

#Left Rotate - TC:O(1),SC:O(1)
def leftRotate(disbalancedNode):
    newRoot=disbalancedNode.rightChild
    disbalancedNode.rightChild=disbalancedNode.rightChild.leftChild
    newRoot.leftChild=disbalancedNode
    disbalancedNode.height=1+max(getHeight(disbalancedNode.rightChild),getHeight(disbalancedNode.leftChild))
    newRoot.height=1+max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode): #TC:O(1)
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) -getHeight(rootNode.rightChild)

def insertNode(rootNode,nodeval): #TC :O(logN),SC:O(logN)
    if not rootNode:
        return AVLNode(nodeval)
    elif nodeval<rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild,nodeval)
    else:
        rootNode.rightChild=insertNode(rootNode.rightChild,nodeval)

    rootNode.height=1+max(getHeight(rootNode.leftChild),getHeight(rootNode.rightChild))
    balance=getBalance(rootNode)
    if balance > 1 and nodeval < rootNode.leftChild.data: #LL condition
        return rightRotate(rootNode)
    if balance > 1 and nodeval > rootNode.leftChild.data: #LR condition
        rootNode.leftChild =leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeval > rootNode.rightChild.data: #RR condition
        return leftRotate(rootNode)
    if balance < -1 and nodeval < rootNode.rightChild.data: #RL condition
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

# Delete a node from AVL Tree - TC:O(logN),SC:O(logN)

def getminValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getminValue(rootNode.leftChild)

def deleteNode(rootNode,nodeval):
    if not rootNode:
        return rootNode
    elif nodeval < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeval)
    elif nodeval > rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild,nodeval)
    # if the node we are deleting has child
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        elif rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp
        """If we delete a node that has 2 childs we need to find the minimum value in the right subtree nd replace the node we want to delete with
        the minimum value node"""
        temp=getminValue(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
        balance=getBalance(rootNode)
        if balance > 1 and getBalance(rootNode.leftChild) >=0: #LL condtion
            return rightRotate(rootNode)
        if balance < -1 and getBalance(rootNode.rightChild) <= 0 : # RR condition
            return leftRotate(rootNode)
        if balance > 1 and getBalance(rootNode.leftChild) < 0: ## LR condition
            rootNode.leftChild=leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        if balance < -1 and getBalance(rootNode.right) < 0: #RL condition
            rootNode.rightChild = rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)

        return rootNode


#Delete Entire AVL tree -  TC:O(1),SC:O(1)
def DeleteEAVL(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "The Avl tree has been Successfully deleted"







newAVL=AVLNode(5)
newAVL=insertNode(newAVL,10)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,20)
levelOrderTraversal(newAVL)
newAVl=deleteNode(newAVL,15)
levelOrderTraversal(newAVL)
DeleteEAVL(newAVL)
levelOrderTraversal(newAVL)





