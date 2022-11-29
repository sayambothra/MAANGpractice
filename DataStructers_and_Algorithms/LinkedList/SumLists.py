from LinkedList_InterViewQuestions import linkedList
# def sumLists(ll1):
#     node=ll1.head
#     sum=""
#     lst=[]
#     while node:
#         print(node.value)
#         lst.append(node.value)
#         node=node.next
#     #print(lst)
#     lst.reverse()
#     #print(lst)
#     for i in range(0,len(lst)):
#         #print(lst[i])
#         sum=sum+str(lst[i])
#     return int(sum)
# CustomLL=linkedList()
# CustomLL.generate(3,0,9)
# num1=sumLists(CustomLL)
# CustomLL1=linkedList()
# CustomLL1.generate(3,0,9)
# num2=sumLists(CustomLL1)
# print(num1)
# print(num2)
#print(num1+num2)
 #Udemy Solution - TC:O(n),SC:O(n)
def SUMLIST(llA,llB):
    n1= llA.head
    n2 = llB.head
    carry =0
    ll=linkedList()
    while n1 or n2:
        result = carry
        result=result+n1.value+n2.value
        n1=n1.next
        n2=n2.next
        ll.add(int(result%10))
        carry=result/10
    return ll

CustomLL1=linkedList()
CustomLL1.generate(3,0,9)
CustomLL2=linkedList()
CustomLL2.generate(3,1,9)
print(CustomLL1)
print(CustomLL2)
print(SUMLIST(CustomLL1,CustomLL2))


