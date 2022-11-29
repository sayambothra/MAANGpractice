'''
CovertString
'''

def findMinOperation(s1,s2,index1,index2):
    if index1==len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1,s2,index1+1,index2+1)
    else:
        DeleteOp= 1 + findMinOperation(s1,s2,index1,index2+1)
        InsertOp= 1 + findMinOperation(s1,s2,index1+1,index2)
        replaceOp=1+findMinOperation(s1,s2,index1+1,index2+1)
        return min(DeleteOp,InsertOp,replaceOp)

print(findMinOperation("table","tgable",0,0))

