from LinkedList_InterViewQuestions import linkedList
#TC:O(n),SC:O(n) Usig Temprary Buffer
def removeDups(ll):
    if ll.head is None:
        return
    else:
        curNode=ll.head
        visited=set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited:
                curNode.next=curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode=curNode.next
        return ll
def removeDups1(ll):
    #TC:O(n^2),SC:O(1)
    if ll.head is None:
        return
    else:
        curNode=ll.head
        while curNode:
            runner=curNode
            while runner.next:
                if runner.next.value  == curNode.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
                curNode=curNode.next
            return ll

customLL=linkedList()
customLL.generate(5,0,10)
print(customLL)
print(removeDups(customLL))

