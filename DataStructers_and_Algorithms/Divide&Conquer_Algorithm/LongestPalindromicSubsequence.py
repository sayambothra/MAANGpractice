def LPS(s1,startindex,endindex):
    s2=""
    if startindex >endindex:
        return 0
    elif startindex == endindex:
        return 1
    elif s1[startindex]==s1[endindex]:

        return 2+LPS(s1,startindex+1,endindex-1)
    else:
        op1=LPS(s1,startindex,endindex-1)
        op2=LPS(s1,startindex+1,endindex)
        return max(op1,op2)

print(LPS("ELRMENMET",0,8))