#Q1.
rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r)) #returns hash value of the dict
print(id(rec))
print(id(r) == id(rec))

#Q2.
a = {(1,2):1,(2,3):2}
print(a[1,2])
#My Output: 1, Actual Output: 1
#Q3.
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
print(id1)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1)
print(id2)
print(id1 == id2)
#My Output: False, Actual Output: True
#Q4.
arr = {}
arr[1] = 1
print(arr)
arr['1'] = 2
print(arr)
arr[1] += 1
print(arr)
sum = 0
for k in arr:
    sum += arr[k]

print(sum)
#My Output:4, Actual Output:4

#Q5.
fruit = {}
def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1


addone('Apple')
addone('Banana')
addone('apple')
print(len(fruit))
#My Output:3 , Actual Output:3

#Q6
# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])
#My Output:Key Error , Actual Output:Key Error

#Q7.
my_dict = {}
my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)
#My Output:30 {(1,2):12,(4,2,1):10,(1,2,4):8)} , Actual Output:Key Error

#Q8.
box = {}
jars = {}
crates = {}
box['biscuit'] = 1
box['cake'] = 3
jars['jam'] = 4
crates['box'] = box
crates['jars'] = jars
#print(len(crates[box]))
#My Output:Type Error,  Actual Output:Type Error

#Q9.
my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
print(my_dict)
sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
#My Output:7 , Actual Output: 6


#Q10.
dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(dict):
    print(dict[_])
#MyOutput: 96 98 97, Actual Output: 96 98 97











