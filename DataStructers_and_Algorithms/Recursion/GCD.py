def greatestCommonDivisor(a,b):
    assert int(a) == a and int(b) == b,'The numbers must be integer only!'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return greatestCommonDivisor(b,a%b)
print(greatestCommonDivisor(48,-18))