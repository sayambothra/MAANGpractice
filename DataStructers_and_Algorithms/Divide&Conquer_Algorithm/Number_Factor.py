'''
Number Factor -

'''

def NumberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1=NumberFactor(n-1)
        subP2=NumberFactor(n-3)
        subP3=NumberFactor(n-4)
        return subP1+subP2+subP3

print(NumberFactor(5))