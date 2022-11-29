lst=[0,1,2,3,4,5,6,7,8]
n=len(lst)
lst1=[]
lst2=[]
lst3=[]

for i in range(0,n):
    if i < n/3:

        lst1.append(lst[i])
    elif i >=n/3 and i <2*(n/3):
        lst2.append(lst[i])
    else:
        lst3.append(lst[i])
lst1.reverse()
lst2.reverse()
lst3.reverse()
print(lst1)
print(lst2)
print(lst3)

#Use a single list to implement three stacks
class multiStack:
    def __init__(self,stacksize):
        self.numberstacks=3
        self.custList=[0] * (stacksize*self.numberstacks)
        self.size=[0] * self.numberstacks
        self.stacksize=stacksize

