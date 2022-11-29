#Creating a dictionary
myDict=dict({"one":"uno","two":"odds"}) #creating adictionary using dict() keyword
newDict={"one":"uno","two":"odds"} # creating in a dictionary using curly braces
print(myDict['one']) # accessiong dictionary values using key - TC:O(1),SC:(1)
print(newDict['two'])

#Update / add an element to the dictionary

myDict1={'name':'Sayam','age':22}
myDict1['age']=23 #updating an Element -TC:O(1),SC:O(1)
print(myDict1)
myDict1['address']='Silicon Valley' #adding element - TC:O(1),SC:amortized O(1)
print(myDict1)

# traversiong through a dictionary - TC:O(n),SC:O(1)
def traverseDict(dict):
    for key in dict:
        print(key,dict[key])
traverseDict(myDict1)

#Searching a value in Dictionary -
def SearchInDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,dict[key]
    return 'value does not exist'
print(SearchInDict(myDict1,'Sayam'))

#Delete an Element - TC:O(1)/Amortized O(n), SC:O(1)
myDict.pop('one') #pop() - takes in key as argument and deletes the key,value pair from the dictionary
print(myDict)
print(myDict1.popitem()) #popitem() -deletes any one of the key,value pairs from the dict
print(myDict1)
myDict1.clear() #clear()-removes all the elemnts from the dictionary
del myDict['two'] #del keyword - we can delete entire dict as well as any item
del myDict # deletes entire dictionary

#Dictionary Methods
myDict2={'name':'Sayam','age':22}
dict1=myDict2.copy() # create a copy of myDict1
print(dict1)
print(myDict2)
newDict1={}.fromkeys([1,2,3],2)
print(newDict1)

print(myDict2.get('name','Sushil')) #get methods return value associated to key if exists or else returns assigned value to the key as given in get method

print(myDict2.items()) # returns a key value pair in a tuple

print(myDict2.keys()) # returns list of keys in the dictionary
myDict2.setdefault('FavouriteVegetable','Cauliflower') # returns the value of key if exist are also it will be inserted in the list
print(myDict2)
print(myDict2.values()) #return a list of values in the dictionary
myDict3={'motherName':'Sarita Bothra','Fathername':'Sushil Bothra'}
print(myDict2.update(myDict3))
print(myDict2)
#in operator in dictionary uses hash table algorithm and TC:O(1)
print('motherName' in myDict2)
Dict = {1: False, 2: False}
print(any(Dict))
print(len(Dict)) #len() - returns no. of pairs
print(sorted(myDict2))# sorted(iterable,reverse=True,key)
