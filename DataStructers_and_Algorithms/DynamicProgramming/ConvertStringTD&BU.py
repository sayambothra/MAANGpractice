'''
Convert_String - BU
'''

def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1) + 1):
        dictKey = str(i1) + '0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2) + 1):
        dictKey = '0' + str(i2)
        tempDict[dictKey] = i2

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dictKey = str(i1) + str(i2)
                dictKey1 = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1) + str(i2)
                dictKeyD = str(i1 - 1) + str(i2)
                dictKeyI = str(i1) + str(i2 - 1)
                dictKeyR = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI], tempDict[dictKeyR]))
    dictKey = str(len(s1)) + str(len(s2))
    return tempDict[dictKey]

#ConvertString - TD
def findMinOperationTD(s1,s2,index1,index2,tempDict):
    if index1 == len(s1):
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1)-index1
    if s1[index1] == s2[index2]:
        return findMinOperationTD(s1,s2,index1+1,index2+1,tempDict)
    else:
        dictKey=str(index1)+str(index2)
        if dictKey not in tempDict:
            DeleteOp=1+findMinOperationTD(s1,s2,index1,index2+1,tempDict)
            InsertOp=1+findMinOperationTD(s1,s2,index1+1,index2,tempDict)
            ReplaceOp=1+findMinOperationTD(s1,s2,index1+1,index2+1,tempDict)
            tempDict[dictKey] = min(DeleteOp,InsertOp,ReplaceOp)
        return tempDict[dictKey]

string1="Sayam"
string2="Sayyam"
print(findMinOperationBU(string1,string2,{}))
print(findMinOperationTD(string1,string2,0,0,{}))