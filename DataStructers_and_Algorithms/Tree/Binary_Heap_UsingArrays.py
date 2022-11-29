#Creation of Binary Heap - TC:O(1),SC:O(n)
class Heap:
    def __init__(self,size):
        self.customList=(size+1)*[None]
        self.heapSize= 0
        self.maxSize=size+1
#Peek of Binary Heap - TC:O(1),SC:O(1)
def Peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

#Size of Heap - TC:O(1),SC:O(1)
def SizeofHeap(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.heapSize

#levelOrderTraversal - TC:O(n),SC:O(1)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

#heapify Method for Insertion - TC:O(logN),SC:O(logN)
def heapifyInsert(rootNode,index, heapType):
    parentIndex=int(index/2)
    if index <= 1:
        return
    if heapType=="Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsert(rootNode,parentIndex,heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,nodeval,heapType): #TC:O(logN),SC:O(logN)
    if rootNode.heapSize+1==rootNode.maxSize:
        return "The heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeval
    rootNode.heapSize+=1
    heapifyInsert(rootNode,rootNode.heapSize,heapType)
    return "The value has been inserted"

#Extract a node from heap - TC:O(logN),SC:O(logN)

def heapifyExtract(rootNode,index,heapType):
    leftIndex=index*2
    rightIndex=index*2 + 1
    swapChild = 0
    #check if rootNode has Children
    if rootNode.heapSize < leftIndex:
        return
    #check if rootNode has only one child and that is leftChild
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    #check if rootNode has 2 children
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild=leftIndex
            else:
                swapChild=rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyExtract(rootNode,swapChild,heapType)



def extractNode(rootNode,heapType):
    if rootNode.heapSize ==0:
        return
    else:
        extractNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize-=1
        heapifyExtract(rootNode,1,heapType)
        return extractNode

#Delete Entire Binary Heap
def DeleteHeap(rootNode):
    rootNode.customList = None
    return "The heap has been deleted"





newBinaryHeap=Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,5,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,1,"Max")
levelOrderTraversal(newBinaryHeap)
extractNode(newBinaryHeap,"Min")
print(SizeofHeap(newBinaryHeap))
levelOrderTraversal(newBinaryHeap)