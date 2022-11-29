from LinkedList_InterViewQuestions import linkedList
def nthElement(ll,location):
    location = len(CustomLL) - location
    if ll.head is None:
        return "The list is Empty"
    else:
        curNode=ll.head
        index = 0
        while curNode:
            if index == location:
                return curNode.value
            curNode=curNode.next
            index+=1
#udemy Solution
def nthToLast(ll,n):
    pointer1=ll.head
    pointer2=ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next
    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1.value
CustomLL=linkedList()
CustomLL.generate(5,0,10)
print(CustomLL)
print(nthElement(CustomLL,2))
print(nthToLast(CustomLL,2))

