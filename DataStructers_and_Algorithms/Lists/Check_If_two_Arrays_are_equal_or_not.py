list1=[1,2,5,4,0]
list2=[2,4,5,1]
def Check_Equal(l1,l2):
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("Yes")
    else:
        print("Not Equal")
Check_Equal(list1,list2)