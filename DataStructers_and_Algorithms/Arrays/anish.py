d={'a' :5, 'b':3,'c' :2}
s=[]
for i in d.keys():
     s+=i*d[i]
     print(s)
     print(d[i])
print(d.keys())
print(s[3::-2])
