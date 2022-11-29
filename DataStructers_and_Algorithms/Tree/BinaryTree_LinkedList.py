#Creation of Binary Tree - TC:O(1),SC:O(1)
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
newTree = TreeNode("Drinks")
leftChild=TreeNode("Hot")
tea=TreeNode("tea")
Coffee=TreeNode("Coffee")
leftChild.leftChild=tea
leftChild.rightChild=Coffee
rightChild=TreeNode("Cold")
newTree.leftChild=leftChild
newTree.rightChild=rightChild


#PreOrder Traversal -  TC:O(n),SC:O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#InOrder Traversal - TC:O(n),SC:O(n)
def InorderTraversal(rootNode):
    if not rootNode:
        return
    InorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    InorderTraversal(rootNode.rightChild)

#PostOrder Traversal - TC:O(n),SC:O(n)
def PostOrderTraversal(rootNode):
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

#Level Order Traversal - TC:O(n),SC:O(n)
import Queue_UsingLL_forTree as q
def LevelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root = CustomQueue.Dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                CustomQueue.Enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                CustomQueue.Enqueue(root.value.rightChild)

#Searching for a node in a Binary Tree - TC:O(n),SC:O(n)
def Search(rootNode,nodevalue):
    if not rootNode:
        return
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while(not CustomQueue.isEmpty()):
            root=CustomQueue.Dequeue()
            if root.value.data == nodevalue:
                return "The node exists in the tree: "
            if (root.value.leftChild is not None):
                CustomQueue.Enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                CustomQueue.Enqueue(root.value.rightChild)
        return "Not Found"

#Insertion of a node in a Binary Tree - TC:O(n),SC:O(n)
def insertNode(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root = CustomQueue.Dequeue()
            if root.value.leftChild is not None:
                CustomQueue.Enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                CustomQueue.Enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"

#Deletion a node from Binary Tree - TC:O(n),SC:O(n)

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root =CustomQueue.Dequeue()
            if (root.value.leftChild is not None):
                CustomQueue.Enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                CustomQueue.Enqueue(root.value.rightChild)
        deepestNode=root.value
        return deepestNode

def DeleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while not (CustomQueue.isEmpty()):
            root=CustomQueue.Dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild =None
                    return
                else:
                    CustomQueue.Enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild =None
                    return
                else:
                    CustomQueue.Enqueue(root.value.leftChild)
def DeleteNode(rootNode,node):
    if not rootNode:
        return
    else:
        CustomQueue=q.Queue()
        CustomQueue.Enqueue(rootNode)
        while not(CustomQueue.isEmpty()):
            root=CustomQueue.Dequeue()
            if root.value.data ==node:
                dNode=getDeepestNode(rootNode)
                root.value.data=dNode.data
                DeleteDeepestNode(rootNode,dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                CustomQueue.Enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                CustomQueue.Enqueue(root.value.rightChild)
        return "Failed to delete"
#delete Entire Binary Tree - TC:O(1),SC:O(1)
def DeleteTree(rootNode):
    if not rootNode:
        return
    else:
        rootNode.data=None
        rootNode.leftChild=None
        rootNode.rightChild=None
        return "The BT has been Successfully deleted"


DeleteTree(newTree)
DeleteNode(newTree,'tea')
deepestNode=getDeepestNode(newTree)
DeleteDeepestNode(newTree,deepestNode)
print(deepestNode.data)
newNode=TreeNode("Cola")
print(insertNode(newTree,newNode))

print(Search(newTree,"tea"))
LevelOrderTraversal(newTree)
preOrderTraversal(newTree)
InorderTraversal(newTree)
PostOrderTraversal(newTree)
