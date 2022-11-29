from LinkedList_InterViewQuestions import linkedList,Node
# def Intersection(llA,llB):
#    if llA.tail is not llB.tail:
#        return False
#    lenA=len(llA)
#    lenB=len(llB)
#
#    shorter=llA if lenA<lenB else llB
#    longer = llB if lenA < lenB else llA
#
#    diff=len(longer)-len(shorter)
#    longerNode=longer.head
#    shorterNode=shorter.head
#
#    for i in range(diff):
#        longerNode=longerNode.next
#
#    while shorterNode is not longerNode:
#        shorterNode=shorterNode.next
#        longerNode=longerNode.next
#    print(longerNode)
#
# def addSameNode(llA,llB,value):
#     tempNode=Node(value)
#     llA.tail.next=tempNode
#     llA.tail=tempNode
#     llB.tail.next = tempNode
#     llB.tail = tempNode
#
#
#
# CustomLL1=linkedList()
# CustomLL2=linkedList()
# CustomLL1.generate(3,0,10)
# CustomLL2.generate(4,0,10)
# addSameNode(CustomLL1,CustomLL2,11)
# addSameNode(CustomLL1,CustomLL2,14)
# print(CustomLL2)
# print(CustomLL1)
# print(Intersection(CustomLL1,CustomLL2))
def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

#def intersection1(llA,llB):



# Helper addition method
def addSameNode(llA, llB, value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = linkedList()
llA.generate(3, 0, 10)

llB = linkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 11)
addSameNode(llA, llB, 14)

print(llA)
print(llB)

print(intersection(llA, llB))


