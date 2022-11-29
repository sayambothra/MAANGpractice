import pyjokes
from collections import Counter,defaultdict,OrderedDict
joke=pyjokes.get_joke('en','neutral')
print(joke)
#Useful modules
li=[1,2,3,4,5,6,7]
sentence='Sayam daddy ka only baby'
print(Counter(li))
print(Counter(sentence))

dictionary=defaultdict(lambda:'does not exist',{'a':1,'b':2})
print(dictionary['c'])
dictionary2=OrderedDict({'c':1,'d':2})
print(dictionary2 ['c'])

dictionary3=OrderedDict({'d':1,'c':2})
print(dictionary3 ['c'])
print(dictionary2==dictionary3)
