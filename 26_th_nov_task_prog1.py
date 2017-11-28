#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
d={'a':1,'b':2,'c':3,'d':5}
s = 0
m=1
for value in d.values():
    s += value
    m *= value
print("Sum of all values in the dict is:",s)
print("The product of all the values in tht dict is:",m)