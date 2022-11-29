from LinkedList_InterViewQuestions import linkedList
def partition(ll,value):
    if ll.head is None:
        return "The List is Empty"
    else:
        curNode=ll.head
        ll.tail=ll.head
        while curNode:
            nextNode=curNode.next
            curNode.next=None
            if curNode.value < value:
                curNode.next=ll.head
                ll.head=curNode
            else:
                ll.tail.next=curNode
                ll.tail=curNode
            curNode=nextNode
        if ll.tail.next is not None:
            ll.tail.next = None
customLL=linkedList()
customLL.generate(5,0,10)
print(customLL)
partition(customLL,6)
print(customLL)












