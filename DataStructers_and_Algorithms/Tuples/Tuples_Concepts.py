#How to Create a Tuple - TC:O(1), SC:O(n)
newTuple=('a','b','c','d','e')
newTuple5=('f','g','h')
print(newTuple)
newTuple2=('a',)
print(newTuple2)
newTuple3=('a') # this is string and not a tuple
print(newTuple3)
newTuple4=tuple() #creating an empty tuple

#Accessing an element in tuple -
print(newTuple[-2])
print(newTuple[1:4])

#Tuple are immutable - Therfore,We cannot update the elements in a tuple

#Traversing a tuple - TC:O(n),SC:O(1)
for i in newTuple:
    print(i)

#Searching for an Element in tuple - TC:O(n),SC:O(1)
print('a' in newTuple) # returns true/false if 'a' exists or not in the tuple
def SearchTuple(tuple,value):
    for i in tuple:
        if i==value:
            return newTuple.index(i)
    return ' Element does not exist'
print(SearchTuple(newTuple,'c'))

#Tuple Operations/Functions -
print(newTuple+newTuple5) #Concates both the tuples and returns a new tuple
print(newTuple5 * 3) # repeat Every element in the newTuple5 for 3 times

print(newTuple5.count('f')) # count() - returns the no. of occurence od the element in the list
print(newTuple5.index('g')) # index() - returns the indices of the element
print(len(newTuple5))#len() - returns no. of elements in the tuple
print(max(newTuple5))#max() - returns maximum element in the tuple
print(min(newTuple5))#min()- returns minimum element in the tuple
print(tuple([1,2,3,4,5]))#tuple() - converts a list to a tuple
