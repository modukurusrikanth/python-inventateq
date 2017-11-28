#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
list_1 = [9, 8, 1, 6, 3, 2, 10, 12, 11, 201, 209, 99, 203,4,-5,4]
print("The list is:", list_1)
req = raw_input("Enter 'a' for ascendin order and 'd' for descending order:")
for i in xrange(len(list_1)):
    for j in xrange(i+1,len(list_1)):
        if req == 'd' or req == 'D':
            if list_1[i] < list_1[j]:
                list_1[i],list_1[j] = list_1[j],list_1[i]
        else:
            if list_1[i] > list_1[j]:
                list_1[i],list_1[j] = list_1[j],list_1[i]
print("the sorted list  is :", list_1)
