#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
### set datat type ########
# go through the link https://www.programiz.com/python-programming/set
# l=[1,2,3,1,3,5,6,7] # set is a mutable data type
# print(set(l)) # if any duplicate elements are there it will remove those values
# a={0,1,2,3}
# b={3,4,5,6,2}
# print("the Uninon of a,b is:",a|b) # when printing a set will not be printing in same order
# print("the Uninon of a,b is:",a.union(b))
# print("the intersection of a,b is:",a&b)
# print("the intersection of a,b is:",a.intersection(b))
# to get difference like uncommon elements
# print("the difference of a,b is:",a-b)
# print("the difference of a,b is:",a.difference(b))
# print("the difference of b,a is:",b-a)
# print("the difference of b,a is:",b.difference(a))
#symmetric difference - it will give unlinke elements in both of sets
# print("the symmetric difference of a,b is:",a^b)
# print("the difference of a,b is:",a.symmetric_difference(b))

# some functions on set
# a1={1,3,4,5}
# a1.add(6) # it will take only one argument if we pass two arguments it will throw error
# print(a1)
# a2={1,25,4,3}
# a2.clear() # clears the set and retruns empty set
# print("after clearing set is :",a2)

# a3={1,25,4,3}
# a4=a3.copy() # uses only values not memory values called shallow copy
# print(a4)

# a5={0,1,2,3}
# b5={3,4,5,6,2}
# a5.difference_update(b5) # Remove all elements of another set from this set
# print(a5)

# a6={0,1,2,3}
# a6.discard(3)  # Remove an element from set if it is a member. (Do nothing if the element is not in set)
# print(a6)

#intersection_update() -> Update the set with the intersection of itself and another
# a7={0,1,2,3}
# b7={3,4,5,6,2}
# a7.intersection_update(b7) # Update the set with the intersection of itself and another
# print(a7)

#isdisjoint()->	Return True if two sets have a null intersection
# a8={0,1,2,3}
# b8={3,4,5,6,2}
# a9={0,1,2,3}
# b9={4,5,6}
# print(a8.isdisjoint(a8&b8)) # gives False here as have common elements
# print(a9.isdisjoint(a9&b9))

#issubset()	-> Return True if another set contains this set
#issuperset()	Return True if this set contains another set
# a9={0,1,2,3,4,5,6}
# b9={4,5}
# print(b9.issubset(a9))
# print(a9.issuperset(b9))

#pop()--->	Remove and return an arbitary set element. Raise KeyError if the set is empty
# a9={0,1,2,3,4,5,6}
# a10={0,1,2,3,4,5,6}
# print(a9.pop())
# print(a9)
# a10.pop()
# print(a10)

#remove()---->	Remove an element from a set. If the element is not a member, raise a KeyError
# a11={0,1,2,3,4,5,6}
# a11.remove(5) # removes 5 from set
# print(a11)
# a11.remove(11) # throws error here

#symmetric_difference_update() --->	Update a set with the symmetric difference of itself and another
# a12={0,1,2,3}
# b12={3,4,5,6,2}
# a12.symmetric_difference_update(b12)
# print(a12)


