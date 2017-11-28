#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
l=[1,5,3]  # initializing a list
# print(l)   # printing a list
# print([1,2,3]+[4,5,6]) # conactenating lists
# print(l*2)  # repetetion of lists
# print(4 in l) # checking membership like eithere it is present or not
# print(3 in l)
# for x in l: # how to ierate a list
#     print(x)
# print(l[:2]) # slicing a list
# del l[2] # deltes the indexed element or throws an error
# print(l)
# print(len(l)) # to get lenght of list
# s="srikanth"
# print(list(s)) # converting tring to a list
# l.append(4) # appending an element to list we can add differet data types also
# print(l)
# print(l.count(1)) # to get the count of an elemnt in a string
# l.extend([4,5,6]) # extending a list
# print("After exteding the list is",l)
# print(l.index(5)) # retruns index if element is there or else throws error
# print(l.find(5)) # find is not there for list
# l.insert(2,(4,5,6)) # as it is it will insert in that index that we pass
# l.insert(2,"test")
# print(l)
# l.extend((1,2,3)) # adding a tuple to
# print(l)
# l.remove(1)# removes if that elements or else throws an exception
# print(l)
# l.pop() # removes the last object and returns the list
# print(l)
# l.pop(1) # removes the object of index and returns that element
# print(l)
# l.reverse() # remove
# print(l)
# l.sort() # sorts in normal order but we need to use either all strings or all integers
# print(l)
# l.sort(reverse=True)
# print(l)
# l.sort(reverse=False)
# print(l)
# l1=['ab','xyz','movie','bangalore','popcorn','X']
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(key=len) # sorts based on length of each element
# print(l1)
# l2=['ab','xyz','mov','bangalore','popcorn','X']
# l2.sort(reverse=True)
# print(l2)
# l3=sorted(l2) # will create a new list and original list will be as it is, we can use it when you dodn't want to change the existing value of data
# print("l2 is",l2)
# print("l3 is",l3)
# l.clear() # to clear everything in the list works in only 3.6 don't works in 2.7
# print(l)
# l2=l.cpoy() #to copy everything in the list to another list works in only 3.6 don't works in 2.7
# print(l2)
# l4=xrange(100) # range() and xrange() function will directly works in 2.7 but in 3.6 we need to convert to that data type
# print(l4)
# l4=range(1,10)
# print(l4)
# l4=range(1,10,3)
# print(l4)
# l4=range(1,10,2)
# print(l4)
l6=[1,3,2,8,4,6]
j=0
for i in range(len(l6)):
    j+= l6[i]
print(j)
# for i in l6:
#     j = j+i
# print(j)
