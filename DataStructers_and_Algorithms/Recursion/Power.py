def PowerOfTwo(n):
    if n==0:
        return 1
    else:
       power=PowerOfTwo(n-1)
       print(power)
       return power*2
print(PowerOfTwo(4))


# Interview Power Question
def Power(x,a):
    assert a>=0 and int(a)==a,'Only Positive Exponenets'
    if a == 0:
        return 1
    else:
        return x*Power(x,a-1)
print(Power(-3,3))