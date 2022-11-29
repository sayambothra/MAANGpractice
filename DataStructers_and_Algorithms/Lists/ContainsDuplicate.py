myList=[1,20,30,44,5,56,57,8,19,10,31,12,13,14,35,16,27,58,19,21]

def isUnique(list):
    a=[]
    for i in myList:
        if i in a:
            print(i)
            return  False
        else:
            a.append(i)
    return True

isUnique(myList)